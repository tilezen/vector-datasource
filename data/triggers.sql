CREATE OR REPLACE FUNCTION mz_trigger_function_landuse()
RETURNS TRIGGER AS $$
BEGIN
    IF mz_calculate_is_landuse(NEW."landuse", NEW."leisure", NEW."natural", NEW."highway", NEW."amenity", NEW."aeroway") then
        NEW.mz_is_landuse := TRUE;
        NEW.mz_centroid := ST_Centroid(NEW.way);
    ELSE
        NEW.mz_is_landuse := NULL;
        NEW.mz_centroid := NULL;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql VOLATILE;

DO $$
BEGIN

PERFORM mz_create_trigger_if_not_exists('mz_trigger_landuse', 'planet_osm_polygon', 'mz_trigger_function_landuse');

END $$;
