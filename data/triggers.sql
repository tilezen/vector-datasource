CREATE OR REPLACE FUNCTION mz_trigger_function_polygon()
RETURNS TRIGGER AS $$
DECLARE
    mz_is_landuse BOOLEAN = mz_calculate_is_landuse(NEW."landuse", NEW."leisure", NEW."natural", NEW."highway", NEW."amenity", NEW."aeroway", NEW."tourism", NEW."man_made", NEW."power", NEW."boundary");
    mz_poi_min_zoom SMALLINT = mz_calculate_poi_level(NEW."aerialway", NEW."aeroway", NEW."amenity", NEW."barrier", NEW."craft", NEW."highway", NEW."historic", NEW."leisure", NEW."lock", NEW."man_made", NEW."natural", NEW."office", NEW."power", NEW."railway", NEW."shop", NEW."tourism", NEW."waterway", NEW.way_area);
BEGIN
    IF mz_is_landuse THEN
        NEW.mz_is_landuse := TRUE;
    ELSE
        NEW.mz_is_landuse := NULL;
    END IF;

    NEW.mz_poi_min_zoom := mz_poi_min_zoom;

    IF mz_is_landuse OR mz_poi_min_zoom IS NOT NULL THEN
        NEW.mz_centroid := ST_Centroid(NEW.way);
    ELSE
        NEW.mz_centroid := NULL;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql VOLATILE;

CREATE TRIGGER mz_trigger_polygon BEFORE INSERT OR UPDATE ON planet_osm_polygon FOR EACH ROW EXECUTE PROCEDURE mz_trigger_function_polygon();

CREATE OR REPLACE FUNCTION mz_trigger_function_point()
RETURNS TRIGGER AS $$
BEGIN
    NEW.mz_poi_min_zoom := mz_calculate_poi_level(NEW."aerialway", NEW."aeroway", NEW."amenity", NEW."barrier", NEW."craft", NEW."highway", NEW."historic", NEW."leisure", NEW."lock", NEW."man_made", NEW."natural", NEW."office", NEW."power", NEW."railway", NEW."shop", NEW."tourism", NEW."waterway", 0::real);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql VOLATILE;

CREATE TRIGGER mz_trigger_point BEFORE INSERT OR UPDATE ON planet_osm_point FOR EACH ROW EXECUTE PROCEDURE mz_trigger_function_point();
