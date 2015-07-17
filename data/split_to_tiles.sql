-- This file contains functions (see `mz_SplitIntoTiles()`) for splitting a
-- table of polygons into uniform tiles. It was useful in integrating the
-- ne_10m_land Natural Earth dataset, which, downloaded straight from the
-- source, stores all seven continents in one monolithic multipolygon. That
-- makes `st_intersects()`/`st_intersection()` take absurdly long, since they
-- can't take advantage of any spatial indexes (which *would* help if it were
-- split up into many smaller polygons), and thus clogs up tile queries, which
-- depend on both of those functions. Hence, we split it into 10km x 10km tiles
-- using `mz_SplitIntoTiles()`.

-- A function that creates a table containing a grid of cells, taken from here:
-- http://gis.stackexchange.com/questions/16374/how-to-create-a-regular-polygon-grid-in-postgis
create or replace function mz_CreateGrid(
	numberX integer,
	numberY integer,
	xsize float8,
	ysize float8,
	x0 float8 default 0,
	y0 float8 default 0,
	out "row" integer,
	out col integer,
	out the_geom geometry
)
returns setof record as
$$
	select
		rowInd + 1 as row,
		colInd + 1 as col,
		st_Translate(cell, colInd * xsize + x0, rowInd * ysize + y0) as the_geom
	from
		generate_series(0, numberY - 1) as rowInd,
		generate_series(0, numberX - 1) as colInd,
		(select (format('POLYGON((0 0, 0 %s, %s %s, %s 0,0 0))', ysize, xsize, ysize, xsize))::geometry as cell) as foo;
$$ language sql immutable strict;

-- Split the polygons in a table called `table_name` into uniformly sized tiles
-- in a table called `${table_name}_tiles`.
create or replace function mz_SplitIntoTiles(
	table_name text,
	tile_size_meters integer,
	geom_column_name text default 'the_geom'
)
returns void as
$$
	declare
		grid_table_name text := table_name || '_grid';
		table_bbox box2d;
		num_tiles_x integer;
		num_tiles_y integer;
	begin
		execute format('select st_extent(%s) from %s', geom_column_name, table_name) into table_bbox;
		num_tiles_x = ceiling(
			(st_xmax(table_bbox) - st_xmin(table_bbox)) / (tile_size_meters :: float)
		);
		num_tiles_y = ceiling(
			(st_ymax(table_bbox) - st_ymin(table_bbox)) / (tile_size_meters :: float)
		);

		-- Create a table containing a grid with cells of length/width
		-- `tile_size_meters`, covering the entire extent of `table_name`.
		execute format(
			'create table %s as
			select *
			from MZ_CreateGrid(%s, %s, %s, %s, %s, %s);',
			grid_table_name, num_tiles_x, num_tiles_y,
			tile_size_meters, tile_size_meters,
			st_xmin(table_bbox), st_ymin(table_bbox)
		);
		perform UpdateGeometrySRID(grid_table_name, 'the_geom', 900913);
		execute format('create index %s_index on %1$s using gist(the_geom)', grid_table_name);

		execute format('create sequence %1$s_ids;', table_name);

		-- Intersect the gridded cells with the polygons in `table_name`,
		-- storing the now-tiled polygons in `${table_name}_tiles`. Assign each
		-- a unique `gid`.
		execute format(
			'create table %1$s_tiles as
			select
				nextval(''%1$s_ids'')::int as gid,
				st_intersection(%1$s.%3$s, %2$s.the_geom) as the_geom
			from %1$s
			join %2$s
			on (
				st_isvalid(%1$s.%3$s) and
				st_intersects(%1$s.%3$s, %2$s.the_geom)
			);',
			table_name, grid_table_name, geom_column_name
		);
		execute format(
			'create index %s_tiles_index on %1$s_tiles using gist(the_geom)',
			table_name
		);

		execute 'drop table ' || grid_table_name;
	end
$$ language plpgsql;
