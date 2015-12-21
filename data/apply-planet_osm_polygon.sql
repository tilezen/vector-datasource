DO $$
BEGIN

--------------------------------------------------------------------------------
-- planet_osm_polygon
--------------------------------------------------------------------------------

-- indexes on existing columns
CREATE INDEX planet_osm_polygon_wayarea_index ON planet_osm_polygon(way_area);
CREATE INDEX planet_osm_polygon_building_index ON planet_osm_polygon(building) WHERE building IS NOT NULL;
CREATE INDEX planet_osm_polygon_admin_level_index ON planet_osm_polygon(admin_level) WHERE boundary = 'administrative';
CREATE INDEX planet_osm_polygon_admin_level_geom_index ON planet_osm_polygon USING gist(way) WHERE boundary = 'administrative';
CREATE INDEX planet_osm_polygon_is_building_or_part_index ON planet_osm_polygon(mz_calculate_is_building_or_part(building, "building:part")) WHERE mz_calculate_is_building_or_part(building, "building:part") = TRUE;

-- update polygon table to add centroids
ALTER TABLE planet_osm_polygon ADD COLUMN mz_is_landuse BOOLEAN;
ALTER TABLE planet_osm_polygon ADD COLUMN mz_poi_min_zoom REAL;
ALTER TABLE planet_osm_polygon ADD COLUMN mz_landuse_min_zoom REAL;

UPDATE planet_osm_polygon SET
    mz_is_landuse = TRUE,
    mz_landuse_min_zoom = mz_calculate_landuse_min_zoom("landuse", "leisure", "natural", "highway", "amenity", "aeroway", "tourism", "man_made", "power", "boundary", way_area)
    WHERE mz_calculate_is_landuse("landuse", "leisure", "natural", "highway", "amenity", "aeroway", "tourism", "man_made", "power", "boundary") = TRUE;

-- the coalesce here is just an optimisation, as the poi level
-- will always be NULL if all of the arguments are NULL.
UPDATE planet_osm_polygon SET
    mz_poi_min_zoom = mz_calculate_poi_level("aerialway", "aeroway", "amenity", "barrier", "craft", "highway", "historic", "leisure", "lock", "man_made", "natural", "office", "power", "railway", "tags"->'rental', "shop", "tourism", "waterway", way_area)
    WHERE coalesce("aerialway", "aeroway", "amenity", "barrier", "craft", "highway", "historic", "leisure", "lock", "man_made", "natural", "office", "power", "railway", "tags"->'rental', "shop", "tourism", "waterway") IS NOT NULL;

CREATE INDEX planet_osm_polygon_is_landuse_col_index ON planet_osm_polygon(mz_is_landuse) WHERE mz_is_landuse=TRUE;

CREATE INDEX planet_osm_polygon_landuse_geom_9_index ON planet_osm_polygon USING gist(way) WHERE mz_is_landuse=TRUE AND mz_landuse_min_zoom <= 9;
CREATE INDEX planet_osm_polygon_landuse_geom_12_index ON planet_osm_polygon USING gist(way) WHERE mz_is_landuse=TRUE AND mz_landuse_min_zoom <= 12;
CREATE INDEX planet_osm_polygon_landuse_geom_15_index ON planet_osm_polygon USING gist(way) WHERE mz_is_landuse=TRUE AND mz_landuse_min_zoom <= 15;

CREATE INDEX planet_osm_polygon_landuse_boundary_geom_4_index ON planet_osm_polygon USING gist(way) WHERE mz_is_landuse=TRUE AND (boundary IN ('national_park', 'protected_area') OR leisure='nature_reserve') AND mz_landuse_min_zoom <= 4;
CREATE INDEX planet_osm_polygon_landuse_boundary_geom_6_index ON planet_osm_polygon USING gist(way) WHERE mz_is_landuse=TRUE AND (boundary IN ('national_park', 'protected_area') OR leisure='nature_reserve') AND mz_landuse_min_zoom <= 6;
CREATE INDEX planet_osm_polygon_landuse_boundary_geom_8_index ON planet_osm_polygon USING gist(way) WHERE mz_is_landuse=TRUE AND (boundary IN ('national_park', 'protected_area') OR leisure='nature_reserve') AND mz_landuse_min_zoom <= 8;

CREATE INDEX planet_osm_polygon_water_geom_index ON planet_osm_polygon USING gist(way) WHERE mz_calculate_is_water("waterway", "natural", "landuse", "amenity", "leisure") = TRUE;

CREATE INDEX planet_osm_polygon_railway_platform_index ON planet_osm_polygon USING gist(way) WHERE railway='platform';

END $$;

ANALYZE planet_osm_polygon;
