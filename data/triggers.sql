CREATE OR REPLACE FUNCTION mz_trigger_function_landuse()
RETURNS TRIGGER AS $$
BEGIN
    IF mz_calculate_is_landuse(NEW."landuse", NEW."leisure", NEW."natural", NEW."highway", NEW."amenity", NEW."aeroway", NEW."tourism", NEW."man_made") then
        NEW.mz_is_landuse := TRUE;
        NEW.mz_centroid := ST_Centroid(NEW.way);
    ELSE
        NEW.mz_is_landuse := NULL;
        NEW.mz_centroid := NULL;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql VOLATILE;

CREATE TRIGGER mz_trigger_landuse BEFORE INSERT OR UPDATE ON planet_osm_polygon FOR EACH ROW EXECUTE PROCEDURE mz_trigger_function_landuse();
