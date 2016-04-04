DO $$
BEGIN

UPDATE ne_110m_ocean SET way_area=ST_Area(the_geom) WHERE the_geom IS NOT NULL;
CREATE INDEX ne_110m_ocean_wayarea_index ON ne_110m_ocean(way_area);

UPDATE ne_110m_lakes SET way_area=ST_Area(the_geom) WHERE the_geom IS NOT NULL;
CREATE INDEX ne_110m_lakes_wayarea_index ON ne_110m_lakes(way_area);

UPDATE ne_50m_ocean SET way_area=ST_Area(the_geom) WHERE the_geom IS NOT NULL;
CREATE INDEX ne_50m_ocean_wayarea_index ON ne_50m_ocean(way_area);

UPDATE ne_50m_lakes SET way_area=ST_Area(the_geom) WHERE the_geom IS NOT NULL;
CREATE INDEX ne_50m_lakes_wayarea_index ON ne_50m_lakes(way_area);

UPDATE ne_50m_playas SET way_area=ST_Area(the_geom) WHERE the_geom IS NOT NULL;
CREATE INDEX ne_50m_playas_wayarea_index ON ne_50m_playas(way_area);

UPDATE ne_10m_ocean SET way_area=ST_Area(the_geom) WHERE the_geom IS NOT NULL;
CREATE INDEX ne_10m_ocean_wayarea_index ON ne_10m_ocean(way_area);

UPDATE ne_10m_lakes SET way_area=ST_Area(the_geom) WHERE the_geom IS NOT NULL;
CREATE INDEX ne_10m_lakes_wayarea_index ON ne_10m_lakes(way_area);

UPDATE ne_10m_playas SET way_area=ST_Area(the_geom) WHERE the_geom IS NOT NULL;
CREATE INDEX ne_10m_playas_wayarea_index ON ne_10m_playas(way_area);

UPDATE ne_10m_urban_areas SET way_area=ST_Area(the_geom) WHERE the_geom IS NOT NULL;
CREATE INDEX ne_10m_urban_areas_way_area_index ON ne_10m_urban_areas(way_area);

UPDATE ne_50m_urban_areas SET way_area=ST_Area(the_geom) WHERE the_geom IS NOT NULL;
CREATE INDEX ne_50m_urban_areas_way_area_index ON ne_50m_urban_areas(way_area);

UPDATE ne_10m_parks_and_protected_lands SET way_area=ST_Area(the_geom) WHERE the_geom IS NOT NULL;
CREATE INDEX ne_10m_parks_and_protected_lands_way_area_index ON ne_10m_parks_and_protected_lands(way_area);

UPDATE water_polygons SET way_area=ST_Area(the_geom) WHERE the_geom IS NOT NULL;
CREATE INDEX water_polygons_wayarea_index ON water_polygons(way_area);


CREATE INDEX ne_10m_populated_places_scalerank_index ON ne_10m_populated_places(scalerank);

END $$;
