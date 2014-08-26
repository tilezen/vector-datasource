-- Sql to execute after all tables have been imported
-- It is safe to re-run

-- used to check whether an index exists before adding
CREATE OR REPLACE FUNCTION mz_does_index_exist(index_name text)
RETURNS BOOLEAN AS $$
BEGIN
    RETURN EXISTS (
        SELECT 1 FROM pg_class AS c
        INNER JOIN pg_namespace AS n ON n.oid = c.relnamespace
        WHERE c.relname = index_name
    );
END;
$$ LANGUAGE plpgsql STABLE;

CREATE OR REPLACE FUNCTION mz_does_trigger_exist(trigger_name text, table_name text)
RETURNS BOOLEAN AS $$
BEGIN
    RETURN EXISTS(
        SELECT 1 FROM pg_class AS c
        INNER JOIN pg_namespace AS n ON n.oid = c.relnamespace
        INNER JOIN pg_trigger AS t ON t.tgrelid = c.oid
        WHERE c.relname = table_name
          AND t.tgname = trigger_name
    );
END;
$$ LANGUAGE plpgsql STABLE;

CREATE OR REPLACE FUNCTION mz_create_index_if_not_exists(index_name text, table_name text, column_name text)
RETURNS VOID AS $$
BEGIN
    IF NOT mz_does_index_exist(index_name) THEN
        EXECUTE 'CREATE INDEX ' ||
            quote_ident(index_name) || ' ON ' || quote_ident(table_name) ||
            '(' || quote_ident(column_name) || ')';
    END IF;
END;
$$ LANGUAGE plpgsql VOLATILE;

CREATE OR REPLACE FUNCTION mz_create_partial_index_if_not_exists(index_name text, table_name text, column_name text, where_clause text)
RETURNS VOID AS $$
BEGIN
    IF NOT mz_does_index_exist(index_name) THEN
        EXECUTE 'CREATE INDEX ' ||
            quote_ident(index_name) || ' ON ' || quote_ident(table_name) ||
            '(' || quote_ident(column_name) || ') WHERE ' || where_clause;
    END IF;
END;
$$ LANGUAGE plpgsql VOLATILE;

CREATE OR REPLACE FUNCTION mz_create_trigger_if_not_exists(
    trigger_name text, table_name text, function_name text)
RETURNS VOID AS $$
BEGIN
    IF NOT mz_does_trigger_exist(trigger_name, table_name) THEN
        EXECUTE 'CREATE TRIGGER ' || quote_ident(trigger_name) ||
          ' BEFORE INSERT OR UPDATE ON ' || quote_ident(table_name) ||
          ' FOR EACH ROW EXECUTE PROCEDURE ' || quote_ident(function_name) || '()';
    END IF;
END;
$$ LANGUAGE plpgsql VOLATILE;

CREATE OR REPLACE FUNCTION mz_does_column_exist(input_table_name text, input_column_name text)
RETURNS BOOLEAN AS $$
BEGIN
    RETURN EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_name=input_table_name AND column_name=input_column_name
    );
END;
$$ LANGUAGE plpgsql STABLE;

CREATE OR REPLACE FUNCTION mz_add_simplified_geometry_column(
    table_name text, column_name text, existing_geom_column_name text, geom_type text, tolerance float, where_clause text default NULL)
RETURNS VOID AS $$
DECLARE v_where_clause TEXT DEFAULT '';
DECLARE v_index_where TEXT DEFAULT '';
BEGIN
    IF NOT mz_does_column_exist(table_name, column_name) THEN
        PERFORM AddGeometryColumn(table_name, column_name, 900913, geom_type, 2);
        IF where_clause IS NOT NULL THEN
            v_where_clause := ' AND ' || where_clause;
            v_index_where := ' WHERE ' || where_clause;
        END IF;
        EXECUTE 'UPDATE ' || quote_ident(table_name) ||
            ' SET ' || quote_ident(column_name) ||
            '=ST_SimplifyPreserveTopology(' || quote_ident(existing_geom_column_name) ||
            ', ' || tolerance || ')' ||
            ' WHERE ' || quote_ident(existing_geom_column_name) || ' IS NOT NULL' ||
            v_where_clause;
        EXECUTE 'CREATE INDEX ' || quote_ident(table_name || '_' || column_name) ||
            ' ON ' || quote_ident(table_name) || ' USING gist(' || quote_ident(column_name) || ')' ||
            v_index_where;
    END IF;
END;
$$ LANGUAGE plpgsql VOLATILE;

CREATE OR REPLACE FUNCTION mz_safe_convert_to_float(v_input text)
RETURNS FLOAT AS $$
DECLARE v_float_value FLOAT DEFAULT NULL;
BEGIN
    BEGIN
        v_float_value := TO_NUMBER(
            REPLACE(REPLACE(v_input, ';', '.'), ',', '.'),
            '999999D99S') AS FLOAT;
    EXCEPTION WHEN OTHERS THEN
        RETURN NULL;
    END;
    RETURN v_float_value;
END;
$$ LANGUAGE plpgsql IMMUTABLE;

CREATE OR REPLACE FUNCTION mz_normalize_id(id bigint, geom Geometry)
RETURNS TEXT AS $$
BEGIN
    IF id < 0 THEN
        RETURN Substr(MD5(ST_AsBinary(geom)), 1, 10);
    ELSE
        RETURN id::text;
    END IF;
END;
$$ LANGUAGE plpgsql STABLE;

CREATE OR REPLACE FUNCTION mz_add_normalized_id(
    table_name text, column_name text, geom_name text, prev_id_column_name text)
RETURNS VOID AS $$
BEGIN
    IF NOT mz_does_column_exist(table_name, column_name) THEN
        EXECUTE 'ALTER TABLE ' || quote_ident(table_name) ||
                ' ADD COLUMN ' || quote_ident(column_name) ||
                ' TEXT';
        EXECUTE 'UPDATE ' || quote_ident(table_name) ||
                ' SET ' || quote_ident(column_name) ||
                ' = mz_normalize_id(' || quote_ident(prev_id_column_name) ||
                ', ' || quote_ident(geom_name) || ')' ||
                ' WHERE ' || quote_ident(prev_id_column_name) || ' IS NOT NULL';
    END IF;
END;
$$ LANGUAGE plpgsql VOLATILE;

CREATE OR REPLACE FUNCTION mz_add_area_column(table_name text, column_name text, geom_name text)
RETURNS VOID AS $$
BEGIN
    IF NOT mz_does_column_exist(table_name, column_name) THEN
        EXECUTE 'ALTER TABLE ' || quote_ident(table_name) ||
                ' ADD COLUMN ' || quote_ident(column_name) ||
                ' REAL';
        EXECUTE 'UPDATE ' || quote_ident(table_name) || ' SET ' || quote_ident(column_name) ||
                ' = ST_Area(' || quote_ident(geom_name) || ') ' ||
                'WHERE ' || quote_ident(geom_name) || ' IS NOT NULL';
    END IF;
END;
$$ LANGUAGE plpgsql VOLATILE;

-- functions to encapsulate logic for calculating new columns

CREATE OR REPLACE FUNCTION mz_calculate_is_landuse(
    landuse_val text, leisure_val text, natural_val text, highway_val text, amenity_val text)
RETURNS BOOLEAN AS $$
BEGIN
    RETURN
        landuse_val IN ('park', 'forest', 'residential', 'retail', 'commercial',
                        'industrial', 'railway', 'cemetery', 'grass', 'farmyard',
                        'farm', 'farmland', 'wood', 'meadow', 'village_green',
                        'recreation_ground', 'allotments', 'quarry')
     OR leisure_val IN ('park', 'garden', 'playground', 'golf_course', 'sports_centre',
                        'pitch', 'stadium', 'common', 'nature_reserve')
     OR natural_val IN ('wood', 'land', 'scrub')
     OR highway_val IN ('pedestrian', 'footway')
     OR amenity_val IN ('university', 'school', 'college', 'library', 'fuel',
                        'parking', 'cinema', 'theatre', 'place_of_worship', 'hospital');
END;
$$ LANGUAGE plpgsql IMMUTABLE;

CREATE OR REPLACE FUNCTION mz_calculate_poi_level(
    aerialway_val text,
    aeroway_val text,
    amenity_val text,
    barrier_val text,
    highway_val text,
    historic_val text,
    leisure_val text,
    lock_val text,
    man_made_val text,
    natural_val text,
    power_val text,
    railway_val text,
    shop_val text,
    tourism_val text,
    waterway_val text
)
RETURNS SMALLINT AS $$
BEGIN
    RETURN (
        CASE WHEN aeroway_val IN ('aerodrome', 'airport') THEN 9
             WHEN natural_val IN ('peak', 'volcano') THEN 11
             WHEN railway_val IN ('station') THEN 12
             WHEN (aerialway_val IN ('station')
                   OR railway_val IN ('halt', 'tram_stop')
                   OR tourism_val IN ('alpine_hut')) THEN 13
             WHEN (natural_val IN ('spring')
                   OR railway_val IN ('level_crossing')) THEN 14
             WHEN (amenity_val IN ('hospital', 'parking')
                   OR barrier_val IN ('gate')
                   OR highway_val IN ('gate', 'mini_roundabout')
                   OR lock_val IN ('yes')
                   OR man_made_val IN ('lighthouse', 'power_wind')
                   OR natural_val IN ('cave_entrance', 'peak', 'spring', 'volcano')
                   OR power_val IN ('generator')
                   OR waterway_val IN ('lock')) THEN 15
             WHEN (aeroway_val IN ('helipad')
                   OR amenity_val IN ('biergarten', 'bus_station', 'bus_stop', 'car_sharing',
                                    'picnic_site', 'place_of_worship',
                                    'prison', 'pub', 'recycling', 'shelter')
                   OR barrier_val IN ('block', 'bollard', 'lift_gate')
                   OR highway_val IN ('bus_stop', 'ford')
                   OR historic_val IN ('archaeological_site')
                   OR man_made_val IN ('windmill')
                   OR natural_val IN ('tree')
                   OR railway_val IN ('halt', 'level_crossing', 'station', 'tram_stop')
                   OR shop_val IN ('department_store', 'supermarket')
                   OR tourism_val IN ('camp_site', 'caravan_site', 'information', 'viewpoint')) THEN 16
             WHEN (amenity_val IN (
                 'atm', 'bank', 'bar', 'bicycle_rental',
                 'cafe', 'cinema', 'courthouse', 'drinking_water', 'embassy', 'emergency_phone',
                 'fast_food', 'fire_station', 'fuel', 'library', 'pharmacy',
                 'police', 'post_box', 'post_office', 'restaurant', 'telephone', 'theatre',
                 'toilets', 'veterinary')
                   OR highway_val IN ('traffic_signals')
                   OR historic_val IN ('memorial')
                   OR leisure_val IN ('playground', 'slipway')
                   OR man_made_val IN ('mast', 'water_tower')
                   OR shop_val IN ('bakery', 'bicycle', 'books', 'butcher', 'car', 'car_repair',
                                 'clothes', 'computer', 'convenience',
                                 'doityourself', 'dry_cleaning', 'fashion', 'florist', 'gift',
                                 'greengrocer', 'hairdresser', 'jewelry', 'mobile_phone',
                                 'optician', 'pet')
                   OR tourism_val IN ('bed_and_breakfast', 'chalet', 'guest_house',
                                    'hostel', 'hotel', 'motel', 'museum')) THEN 17
             WHEN (amenity_val IN ('bench', 'waste_basket')
                   OR railway_val IN ('subway_entrance')) THEN 18
             ELSE NULL END
    );
END;
$$ LANGUAGE plpgsql IMMUTABLE;

CREATE OR REPLACE FUNCTION mz_calculate_road_level(highway_val text, railway_val text)
RETURNS SMALLINT AS $$
BEGIN
    RETURN (
        CASE WHEN highway_val IN ('motorway') THEN 7
             WHEN highway_val IN ('trunk', 'primary', 'secondary') THEN 10
             WHEN highway_val IN ('tertiary') THEN 11
             WHEN highway_val IN ('motorway_link', 'trunk_link', 'residential', 'unclassified', 'road') THEN 12
             WHEN highway_val IN ('primary_link', 'secondary_link') THEN 13
             WHEN (highway_val IN ('tertiary_link', 'minor')
                OR railway_val IN ('rail')) THEN 14
             WHEN (highway_val IN ('service', 'footpath', 'track', 'footway', 'steps', 'pedestrian', 'path', 'cycleway')
                OR railway_val IN ('tram', 'light_rail', 'narrow_gauge', 'monorail')) THEN 15
             ELSE NULL END
    );
END;
$$ LANGUAGE plpgsql IMMUTABLE;

CREATE OR REPLACE FUNCTION mz_calculate_road_sort_key(
    layer_val text, bridge_val text, tunnel_val text, highway_val text, railway_val text)
RETURNS FLOAT AS $$
DECLARE v_layer_as_float FLOAT DEFAULT NULL;
BEGIN
    v_layer_as_float := mz_safe_convert_to_float(layer_val);
    RETURN (
        (CASE WHEN v_layer_as_float IS NOT NULL THEN 1000 * v_layer_as_float
            ELSE 0
            END)

        +

        --
        -- Bridges and tunnels have an implicit physical layering.
        --
        (CASE WHEN bridge_val IN ('yes', 'true') THEN 100
            WHEN tunnel_val IN ('yes', 'true') THEN -100
            ELSE 0
            END)

        +

        --
        -- Large roads are drawn on top of smaller roads.
        --
        (CASE WHEN highway_val IN ('motorway') THEN 0
            WHEN railway_val IN ('rail', 'tram', 'light_rail', 'narrow_guage', 'monorail') THEN -.5
            WHEN highway_val IN ('trunk') THEN -1
            WHEN highway_val IN ('primary') THEN -2
            WHEN highway_val IN ('secondary') THEN -3
            WHEN highway_val IN ('tertiary') THEN -4
            WHEN highway_val LIKE '%_link' THEN -5
            WHEN highway_val IN ('residential', 'unclassified', 'road') THEN -6
            WHEN highway_val IN ('unclassified', 'service', 'minor') THEN -7
            ELSE -9 END)
    );
END;
$$ LANGUAGE plpgsql IMMUTABLE;

CREATE OR REPLACE FUNCTION mz_calculate_is_water(
    waterway_val text, natural_val text, landuse_val text)
RETURNS BOOLEAN AS $$
BEGIN
    RETURN (
        waterway_val IN ('riverbank')
     OR natural_val IN ('water')
     OR landuse_val IN ('basin', 'reservoir')
    );
END;
$$ LANGUAGE plpgsql IMMUTABLE;

CREATE OR REPLACE FUNCTION mz_calculate_is_building_or_part(
    building_val text, buildingpart_val text)
RETURNS BOOLEAN AS $$
BEGIN
    RETURN (building_val IS NOT NULL OR buildingpart_val IS NOT NULL);
END;
$$ LANGUAGE plpgsql IMMUTABLE;

-- functions to temporarily enable and disable triggers
-- prevents them from firing while executing mass updates

CREATE OR REPLACE FUNCTION mz_tables_with_triggers()
RETURNS TEXT[] AS $$
BEGIN
    RETURN ARRAY['planet_osm_polygon', 'planet_osm_line', 'planet_osm_point', 'water_polygons'];
END;
$$ LANGUAGE plpgsql IMMUTABLE;

CREATE OR REPLACE FUNCTION mz_disable_triggers()
RETURNS VOID AS $$
DECLARE table_name TEXT;
BEGIN
    FOREACH table_name IN ARRAY mz_tables_with_triggers()
    LOOP
        EXECUTE 'ALTER TABLE ' || quote_ident(table_name) ||
                ' DISABLE TRIGGER USER';
    END LOOP;
END;
$$ LANGUAGE plpgsql VOLATILE;

CREATE OR REPLACE FUNCTION mz_enable_triggers()
RETURNS VOID AS $$
DECLARE table_name TEXT;
BEGIN
    FOREACH table_name IN ARRAY mz_tables_with_triggers()
    LOOP
        EXECUTE 'ALTER TABLE ' || quote_ident(table_name) ||
                ' ENABLE TRIGGER USER';
    END LOOP;
END;
$$ LANGUAGE plpgsql VOLATILE;

-- create additional columns
-- will also execute the relevant update to populate the column with data
DO $$
BEGIN

PERFORM mz_disable_triggers();

-- add way_area columns to tables that don't have it
PERFORM mz_add_area_column('ne_110m_ocean', 'way_area', 'the_geom');
PERFORM mz_add_area_column('ne_110m_lakes', 'way_area', 'the_geom');
PERFORM mz_add_area_column('ne_50m_ocean', 'way_area', 'the_geom');
PERFORM mz_add_area_column('ne_50m_lakes', 'way_area', 'the_geom');
PERFORM mz_add_area_column('ne_50m_playas', 'way_area', 'the_geom');
PERFORM mz_add_area_column('ne_10m_ocean', 'way_area', 'the_geom');
PERFORM mz_add_area_column('ne_10m_lakes', 'way_area', 'the_geom');
PERFORM mz_add_area_column('ne_10m_playas', 'way_area', 'the_geom');
PERFORM mz_add_area_column('water_polygons', 'way_area', 'the_geom');
PERFORM mz_add_area_column('ne_10m_urban_areas', 'way_area', 'the_geom');
PERFORM mz_add_area_column('ne_50m_urban_areas', 'way_area', 'the_geom');
PERFORM mz_add_area_column('ne_10m_parks_and_protected_lands', 'way_area', 'the_geom');

-- ensure building height is a float for queries
IF NOT mz_does_column_exist('planet_osm_polygon', 'mz_height') THEN
    ALTER TABLE planet_osm_polygon ADD COLUMN mz_height FLOAT;
    UPDATE planet_osm_polygon SET mz_height=mz_safe_convert_to_float(height)
        WHERE height IS NOT NULL;
END IF;

-- ditto for building min height
IF NOT mz_does_column_exist('planet_osm_polygon', 'mz_min_height') THEN
    ALTER TABLE planet_osm_polygon ADD COLUMN mz_min_height FLOAT;
    UPDATE planet_osm_polygon SET mz_min_height=mz_safe_convert_to_float(min_height)
        WHERE min_height IS NOT NULL;
END IF;

-- normalize osm_id
PERFORM mz_add_normalized_id('planet_osm_polygon', 'mz_id', 'way', 'osm_id');
PERFORM mz_add_normalized_id('planet_osm_line', 'mz_id', 'way', 'osm_id');
PERFORM mz_add_normalized_id('planet_osm_point', 'mz_id', 'way', 'osm_id');

-- tag whether the record is relevant for landuse queries
IF NOT mz_does_column_exist('planet_osm_polygon', 'mz_is_landuse') THEN
    ALTER TABLE planet_osm_polygon ADD COLUMN mz_is_landuse BOOLEAN;
    UPDATE planet_osm_polygon SET mz_is_landuse = TRUE WHERE
        mz_calculate_is_landuse(
            "landuse", "leisure", "natural", "highway", "amenity") = TRUE;
END IF;

-- tag whether the record is a poi, relevant for the particular zoom level
IF NOT mz_does_column_exist('planet_osm_point', 'mz_poi_level') THEN
    ALTER TABLE planet_osm_point ADD COLUMN mz_poi_level SMALLINT;
    UPDATE planet_osm_point SET
        mz_poi_level = mz_calculate_poi_level(
            "aerialway",
            "aeroway",
            "amenity",
            "barrier",
            "highway",
            "historic",
            "leisure",
            "lock",
            "man_made",
            "natural",
            "power",
            "railway",
            "shop",
            "tourism",
            "waterway"
        );
END IF;

-- tag whether the record is relevant for road queries at the appropriate zoom
IF NOT mz_does_column_exist('planet_osm_line', 'mz_road_level') THEN
    ALTER TABLE planet_osm_line ADD COLUMN mz_road_level SMALLINT;
    UPDATE planet_osm_line
        SET mz_road_level = mz_calculate_road_level(highway, railway);
END IF;

-- pre-compute the sort key for roads
IF NOT mz_does_column_exist('planet_osm_line', 'mz_road_sort_key') THEN
    ALTER TABLE planet_osm_line ADD COLUMN mz_road_sort_key FLOAT;
    UPDATE planet_osm_line
        SET mz_road_sort_key = mz_calculate_road_sort_key(
            layer, bridge, tunnel, highway, railway)
        WHERE mz_road_level IS NOT NULL;
END IF;

-- tag whether the record is relevant for water queries
IF NOT mz_does_column_exist('planet_osm_polygon', 'mz_is_water') THEN
    ALTER TABLE planet_osm_polygon ADD COLUMN mz_is_water BOOLEAN;
    UPDATE planet_osm_polygon
        SET mz_is_water = TRUE
        WHERE mz_calculate_is_water("waterway", "natural", "landuse");
END IF;

-- tag whether the record is relevant for building queries
IF NOT mz_does_column_exist('planet_osm_polygon', 'mz_is_building_or_part') THEN
    ALTER TABLE planet_osm_polygon ADD COLUMN mz_is_building_or_part BOOLEAN;
    UPDATE planet_osm_polygon
        SET mz_is_building_or_part = TRUE
        WHERE mz_calculate_is_building_or_part(building, "building:part");
END IF;

PERFORM mz_enable_triggers();

END$$;

-- add indexes to tables
DO $$
BEGIN

-- way_area indexes
PERFORM mz_create_index_if_not_exists('ne_110m_ocean_wayarea_index', 'ne_110m_ocean', 'way_area');
PERFORM mz_create_index_if_not_exists('ne_110m_lakes_wayarea_index', 'ne_110m_lakes', 'way_area');
PERFORM mz_create_index_if_not_exists('ne_50m_ocean_wayarea_index', 'ne_50m_ocean', 'way_area');
PERFORM mz_create_index_if_not_exists('ne_50m_lakes_wayarea_index', 'ne_50m_lakes', 'way_area');
PERFORM mz_create_index_if_not_exists('ne_50m_playas_wayarea_index', 'ne_50m_playas', 'way_area');
PERFORM mz_create_index_if_not_exists('ne_50m_urban_areas_way_area_index', 'ne_50m_urban_areas', 'way_area');
PERFORM mz_create_index_if_not_exists('ne_10m_ocean_wayarea_index', 'ne_10m_ocean', 'way_area');
PERFORM mz_create_index_if_not_exists('ne_10m_lakes_wayarea_index', 'ne_10m_lakes', 'way_area');
PERFORM mz_create_index_if_not_exists('ne_10m_playas_wayarea_index', 'ne_10m_playas', 'way_area');
PERFORM mz_create_index_if_not_exists('ne_10m_urban_areas_way_area_index', 'ne_10m_urban_areas', 'way_area');
PERFORM mz_create_index_if_not_exists('ne_10m_parks_and_protected_lands_way_area_index', 'ne_10m_parks_and_protected_lands', 'way_area');
PERFORM mz_create_index_if_not_exists('water_polygons_wayarea_index', 'water_polygons', 'way_area');
PERFORM mz_create_index_if_not_exists('planet_osm_polygon_wayarea_index', 'planet_osm_polygon', 'way_area');

-- indexes for existing columns
PERFORM mz_create_index_if_not_exists('planet_osm_polygon_building_index', 'planet_osm_polygon', 'building');
PERFORM mz_create_partial_index_if_not_exists('planet_osm_polygon_admin_level_index', 'planet_osm_polygon', 'admin_level', 'boundary = ''administrative''');
PERFORM mz_create_partial_index_if_not_exists('planet_osm_point_place', 'planet_osm_point', 'place',
    'name is NOT NULL' );

-- indexes for new columns
PERFORM mz_create_index_if_not_exists('planet_osm_polygon_mz_is_landuse_index', 'planet_osm_polygon', 'mz_is_landuse');
PERFORM mz_create_index_if_not_exists('planet_osm_polygon_mz_is_water_index', 'planet_osm_polygon', 'mz_is_water');
PERFORM mz_create_index_if_not_exists('planet_osm_point_mz_poi_level_index', 'planet_osm_point', 'mz_poi_level');
PERFORM mz_create_index_if_not_exists('planet_osm_polygon_mz_road_level_index', 'planet_osm_line', 'mz_road_level');
PERFORM mz_create_index_if_not_exists('planet_osm_polygon_mz_is_building_or_part_index', 'planet_osm_polygon', 'mz_is_building_or_part');

END$$;

DO $$
BEGIN

PERFORM mz_disable_triggers();

-- geometry simplifications

PERFORM mz_add_simplified_geometry_column('planet_osm_polygon', 'mz_way14', 'way', 'Geometry', 9.55,
    'building IS NOT NULL');
PERFORM mz_add_simplified_geometry_column('planet_osm_polygon', 'mz_way12', 'way', 'Geometry', 38.22,
    'mz_is_water=TRUE');
PERFORM mz_add_simplified_geometry_column('planet_osm_polygon', 'mz_way11', 'way', 'Geometry', 76.44,
    'mz_is_landuse=TRUE');
PERFORM mz_add_simplified_geometry_column('water_polygons', 'mz_the_geom12', 'the_geom', 'Geometry', 38.22);

PERFORM mz_enable_triggers();

END$$;

-- functions that triggers use
CREATE OR REPLACE FUNCTION mz_trigger_function_building()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.height IS NULL THEN
        NEW.mz_height := NULL;
    ELSE
        NEW.mz_height := mz_safe_convert_to_float(NEW.height);
    END IF;
    IF NEW.min_height IS NULL THEN
        NEW.mz_min_height := NULL;
    ELSE
        NEW.mz_min_height := mz_safe_convert_to_float(NEW.min_height);
    END IF;
    IF mz_calculate_is_building_or_part(NEW.building, NEW."building:part") THEN
        NEW.mz_is_building_or_part := TRUE;
    ELSE
        NEW.mz_is_building_or_part := NULL;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql VOLATILE;

CREATE OR REPLACE FUNCTION mz_trigger_function_id()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.osm_id IS NULL THEN
        NEW.mz_id := NULL;
    ELSE
        NEW.mz_id := mz_normalize_id(NEW.osm_id, NEW.way);
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql VOLATILE;

CREATE OR REPLACE FUNCTION mz_trigger_function_is_landuse()
RETURNS TRIGGER AS $$
BEGIN
    IF mz_calculate_is_landuse(
        NEW."landuse", NEW."leisure", NEW."natural", NEW."highway", NEW."amenity") THEN
        NEW.mz_is_landuse := TRUE;
    ELSE
        NEW.mz_is_landuse := NULL;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql VOLATILE;

CREATE OR REPLACE FUNCTION mz_trigger_function_poi_level()
RETURNS TRIGGER AS $$
BEGIN
    NEW.mz_poi_level := mz_calculate_poi_level(
        NEW."aerialway",
        NEW."aeroway",
        NEW."amenity",
        NEW."barrier",
        NEW."highway",
        NEW."historic",
        NEW."leisure",
        NEW."lock",
        NEW."man_made",
        NEW."natural",
        NEW."power",
        NEW."railway",
        NEW."shop",
        NEW."tourism",
        NEW."waterway"
    );
    RETURN NEW;
END;
$$ LANGUAGE plpgsql VOLATILE;

CREATE OR REPLACE FUNCTION mz_trigger_function_road()
RETURNS TRIGGER AS $$
BEGIN
    NEW.mz_road_level := mz_calculate_road_level(NEW.highway, NEW.railway);
    IF NEW.mz_road_level IS NOT NULL THEN
        NEW.mz_road_sort_key := mz_calculate_road_sort_key(
            NEW.layer,
            NEW.bridge,
            NEW.tunnel,
            NEW.highway,
            NEW.railway
        );
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql VOLATILE;

CREATE OR REPLACE FUNCTION mz_trigger_function_is_water()
RETURNS TRIGGER AS $$
BEGIN
    NEW.mz_is_water := mz_calculate_is_water(
        NEW."waterway",
        NEW."natural",
        NEW."landuse"
    );
    RETURN NEW;
END;
$$ LANGUAGE plpgsql VOLATILE;

-- geometry simplification triggers
CREATE OR REPLACE FUNCTION mz_trigger_function_geometry_building()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.building is NOT NULL THEN
        NEW.mz_way14 := ST_SimplifyPreserveTopology(NEW.way, 9.55);
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql VOLATILE;

CREATE OR REPLACE FUNCTION mz_trigger_function_geometry_water()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.mz_is_water = TRUE THEN
        NEW.mz_way12 := ST_SimplifyPreserveTopology(NEW.way, 38.22);
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql VOLATILE;

CREATE OR REPLACE FUNCTION mz_trigger_function_geometry_landuse()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.mz_is_landuse = TRUE THEN
        NEW.mz_way11 := ST_SimplifyPreserveTopology(NEW.way, 76.44);
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql VOLATILE;

CREATE OR REPLACE FUNCTION mz_trigger_function_geometry_water_polygons()
RETURNS TRIGGER AS $$
BEGIN
    NEW.mz_the_geom12 := ST_SimplifyPreserveTopology(NEW.the_geom, 38.22);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql VOLATILE;

DO $$
BEGIN

-- create the actual triggers
PERFORM mz_create_trigger_if_not_exists(
    'mz_trigger_building', 'planet_osm_polygon', 'mz_trigger_function_building');

PERFORM mz_create_trigger_if_not_exists(
    'mz_trigger_id_line', 'planet_osm_line', 'mz_trigger_function_id');
PERFORM mz_create_trigger_if_not_exists(
    'mz_trigger_id_polygon', 'planet_osm_polygon', 'mz_trigger_function_id');
PERFORM mz_create_trigger_if_not_exists(
    'mz_trigger_id_point', 'planet_osm_point', 'mz_trigger_function_id');

PERFORM mz_create_trigger_if_not_exists(
    'mz_trigger_is_landuse', 'planet_osm_polygon', 'mz_trigger_function_is_landuse');

PERFORM mz_create_trigger_if_not_exists(
    'mz_trigger_poi_level', 'planet_osm_point', 'mz_trigger_function_poi_level');

PERFORM mz_create_trigger_if_not_exists(
    'mz_trigger_road', 'planet_osm_line', 'mz_trigger_function_road');

PERFORM mz_create_trigger_if_not_exists(
    'mz_trigger_is_water', 'planet_osm_polygon', 'mz_trigger_function_is_water');

-- add geometry simplification triggers
PERFORM mz_create_trigger_if_not_exists(
    'mz_trigger_z_geometry_building', 'planet_osm_polygon', 'mz_trigger_function_geometry_building');

PERFORM mz_create_trigger_if_not_exists(
    'mz_trigger_z_geometry_water', 'planet_osm_polygon', 'mz_trigger_function_geometry_water');

PERFORM mz_create_trigger_if_not_exists(
    'mz_trigger_z_geometry_landuse', 'planet_osm_polygon', 'mz_trigger_function_geometry_landuse');

PERFORM mz_create_trigger_if_not_exists(
    'mz_trigger_z_geometry_water_polygons', 'water_polygons', 'mz_trigger_function_geometry_water_polygons');

END $$;
