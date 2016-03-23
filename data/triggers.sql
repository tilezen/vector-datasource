CREATE OR REPLACE FUNCTION mz_trigger_function_polygon()
RETURNS TRIGGER AS $$
BEGIN
    NEW.mz_poi_min_zoom := mz_calculate_min_zoom_pois(NEW.*);
    NEW.mz_landuse_min_zoom := mz_calculate_min_zoom_landuse(NEW.*);
    NEW.mz_transit_level := mz_calculate_min_zoom_transit(NEW.*);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql VOLATILE;

-- do a drop-if-exists + create in a transaction to ensure that the script
-- is idempotent.
BEGIN;
DROP TRIGGER IF EXISTS mz_trigger_polygon ON planet_osm_polygon;
CREATE TRIGGER mz_trigger_polygon BEFORE INSERT OR UPDATE ON planet_osm_polygon FOR EACH ROW EXECUTE PROCEDURE mz_trigger_function_polygon();
COMMIT;

CREATE OR REPLACE FUNCTION mz_trigger_function_point()
RETURNS TRIGGER AS $$
BEGIN
    NEW.mz_poi_min_zoom := mz_calculate_min_zoom_pois(NEW.*);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql VOLATILE;

-- do a drop-if-exists + create in a transaction to ensure that the script
-- is idempotent.
BEGIN;
DROP TRIGGER IF EXISTS mz_trigger_point ON planet_osm_point;
CREATE TRIGGER mz_trigger_point BEFORE INSERT OR UPDATE ON planet_osm_point FOR EACH ROW EXECUTE PROCEDURE mz_trigger_function_point();
COMMIT;

CREATE OR REPLACE FUNCTION mz_trigger_function_line()
RETURNS TRIGGER AS $$
BEGIN
    NEW.mz_road_level := mz_calculate_road_level(NEW."highway", NEW."railway", NEW."aeroway", NEW."route", NEW."service", NEW."aerialway", NEW."leisure", NEW."sport", NEW."man_made", NEW."way");
    NEW.mz_transit_level := mz_calculate_min_zoom_transit(NEW.*);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql VOLATILE;

-- do a drop-if-exists + create in a transaction to ensure that the script
-- is idempotent.
BEGIN;
DROP TRIGGER IF EXISTS mz_trigger_line ON planet_osm_line;
CREATE TRIGGER mz_trigger_line BEFORE INSERT OR UPDATE ON planet_osm_line FOR EACH ROW EXECUTE PROCEDURE mz_trigger_function_line();
COMMIT;
