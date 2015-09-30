DO $$
BEGIN

--------------------------------------------------------------------------------
-- planet_osm_polygon
--------------------------------------------------------------------------------

-- indexes on existing columns
CREATE INDEX planet_osm_polygon_wayarea_index ON planet_osm_polygon(way_area);
CREATE INDEX planet_osm_polygon_building_index ON planet_osm_polygon(building) WHERE building IS NOT NULL;
CREATE INDEX planet_osm_polygon_admin_level_index ON planet_osm_polygon(admin_level) WHERE boundary = 'administrative';
CREATE INDEX planet_osm_polygon_is_building_or_part_index ON planet_osm_polygon(mz_calculate_is_building_or_part(building, "building:part")) WHERE mz_calculate_is_building_or_part(building, "building:part") = TRUE;
CREATE INDEX planet_osm_polygon_is_water_index ON planet_osm_polygon(mz_calculate_is_water("waterway", "natural", "landuse")) WHERE mz_calculate_is_water("waterway", "natural", "landuse") = TRUE;

-- update polygon table to add centroids
ALTER TABLE planet_osm_polygon ADD COLUMN mz_is_landuse BOOLEAN;
ALTER TABLE planet_osm_polygon ADD COLUMN mz_centroid GEOMETRY;
ALTER TABLE planet_osm_polygon ADD COLUMN mz_poi_min_zoom REAL;
ALTER TABLE planet_osm_polygon ADD COLUMN mz_landuse_min_zoom REAL;

UPDATE planet_osm_polygon SET
    mz_is_landuse = TRUE,
    mz_landuse_min_zoom = mz_calculate_landuse_min_zoom("landuse", "leisure", "natural", "highway", "amenity", "aeroway", "tourism", "man_made", "power", "boundary", way_area)
    WHERE mz_calculate_is_landuse("landuse", "leisure", "natural", "highway", "amenity", "aeroway", "tourism", "man_made", "power", "boundary") = TRUE;

-- the coalesce here is just an optimisation, as the poi level
-- will always be NULL if all of the arguments are NULL.
UPDATE planet_osm_polygon SET
    mz_poi_min_zoom = mz_calculate_poi_level("aerialway", "aeroway", "amenity", "barrier", "craft", "highway", "historic", "leisure", "lock", "man_made", "natural", "office", "power", "railway", "shop", "tourism", "waterway", way_area)
    WHERE coalesce("aerialway", "aeroway", "amenity", "barrier", "craft", "highway", "historic", "leisure", "lock", "man_made", "natural", "office", "power", "railway", "shop", "tourism", "waterway") IS NOT NULL;

-- at the moment we only add centroids to landuse or POI features
UPDATE planet_osm_polygon SET
    mz_centroid = ST_Centroid(way)
    WHERE mz_is_landuse = TRUE
       OR mz_poi_min_zoom IS NOT NULL;


CREATE INDEX planet_osm_polygon_is_landuse_col_index ON planet_osm_polygon(mz_is_landuse) WHERE mz_is_landuse=TRUE;
CREATE INDEX planet_osm_polygon_centroid_landuse_index ON planet_osm_polygon USING gist(mz_centroid) WHERE mz_is_landuse=TRUE;

END $$;
