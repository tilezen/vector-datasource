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

-- tolerances are calculated as follows
-- [6378137 * 2 * pi / (2 ** (zoom + 8)) for zoom in range(22)]
-- zoom level  0: 156543.033928
-- zoom level  1: 78271.516964
-- zoom level  2: 39135.758482
-- zoom level  3: 19567.879241
-- zoom level  4: 9783.9396205
-- zoom level  5: 4891.96981025
-- zoom level  6: 2445.98490513
-- zoom level  7: 1222.99245256
-- zoom level  8: 611.496226281
-- zoom level  9: 305.748113141
-- zoom level 10: 152.87405657
-- zoom level 11: 76.4370282852
-- zoom level 12: 38.2185141426
-- zoom level 13: 19.1092570713
-- zoom level 14: 9.55462853565
-- zoom level 15: 4.77731426782
-- zoom level 16: 2.38865713391
-- zoom level 17: 1.19432856696
-- zoom level 18: 0.597164283478
-- zoom level 19: 0.298582141739
-- zoom level 20: 0.149291070869
-- zoom level 21: 0.0746455354347

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

END $$;
