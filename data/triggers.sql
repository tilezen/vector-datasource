CREATE OR REPLACE FUNCTION mz_trigger_function_polygon()
RETURNS TRIGGER AS $$
DECLARE
    mz_is_landuse BOOLEAN = mz_calculate_is_landuse(NEW."landuse", NEW."leisure", NEW."natural", NEW."highway", NEW."amenity", NEW."aeroway", NEW."tourism", NEW."man_made", NEW."power", NEW."boundary");
    mz_poi_min_zoom REAL = mz_calculate_poi_level(NEW."aerialway", NEW."aeroway", NEW."amenity", NEW."barrier", NEW."craft", NEW."highway", NEW."historic", NEW."leisure", NEW."lock", NEW."man_made", NEW."natural", NEW."office", NEW."power", NEW."railway", NEW."tags"->'rental', NEW."shop", NEW."tourism", NEW."waterway", NEW.way_area);
BEGIN
    IF mz_is_landuse THEN
        NEW.mz_is_landuse := TRUE;
        NEW.mz_landuse_min_zoom := mz_calculate_landuse_min_zoom(NEW."landuse", NEW."leisure", NEW."natural", NEW."highway", NEW."amenity", NEW."aeroway", NEW."tourism", NEW."man_made", NEW."power", NEW."boundary", NEW.way_area);
    ELSE
        NEW.mz_is_landuse := NULL;
        NEW.mz_landuse_min_zoom := NULL;
    END IF;

    NEW.mz_poi_min_zoom := mz_poi_min_zoom;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql VOLATILE;

CREATE TRIGGER mz_trigger_polygon BEFORE INSERT OR UPDATE ON planet_osm_polygon FOR EACH ROW EXECUTE PROCEDURE mz_trigger_function_polygon();

CREATE OR REPLACE FUNCTION mz_trigger_function_point()
RETURNS TRIGGER AS $$
BEGIN
    NEW.mz_poi_min_zoom := mz_calculate_poi_level(NEW."aerialway", NEW."aeroway", NEW."amenity", NEW."barrier", NEW."craft", NEW."highway", NEW."historic", NEW."leisure", NEW."lock", NEW."man_made", NEW."natural", NEW."office", NEW."power", NEW."railway", NEW."tags"->'rental', NEW."shop", NEW."tourism", NEW."waterway", 0::real);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql VOLATILE;

CREATE TRIGGER mz_trigger_point BEFORE INSERT OR UPDATE ON planet_osm_point FOR EACH ROW EXECUTE PROCEDURE mz_trigger_function_point();

CREATE OR REPLACE FUNCTION mz_trigger_function_line()
RETURNS TRIGGER AS $$
BEGIN
    NEW.mz_road_level := mz_calculate_road_level(NEW."highway", NEW."railway", NEW."aeroway", NEW."route", NEW."service", NEW."aerialway", NEW."leisure", NEW."sport", NEW."man_made", NEW."way");
    NEW.mz_transit_level := mz_calculate_transit_level(NEW."route");
    RETURN NEW;
END;
$$ LANGUAGE plpgsql VOLATILE;

CREATE TRIGGER mz_trigger_line BEFORE INSERT OR UPDATE ON planet_osm_line FOR EACH ROW EXECUTE PROCEDURE mz_trigger_function_line();
