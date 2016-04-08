CREATE OR REPLACE FUNCTION mz_trigger_function_polygon()
RETURNS TRIGGER AS $$
BEGIN
    NEW.mz_poi_min_zoom := mz_calculate_min_zoom_pois(NEW.*);
    NEW.mz_landuse_min_zoom := mz_calculate_min_zoom_landuse(NEW.*);
    NEW.mz_transit_level := mz_calculate_min_zoom_transit(NEW.*);
    NEW.mz_water_min_zoom := mz_calculate_min_zoom_water(NEW.*);
    NEW.mz_boundary_min_zoom := mz_calculate_min_zoom_boundaries(NEW.*);
    NEW.mz_building_min_zoom := mz_calculate_min_zoom_buildings(NEW.*);
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
    NEW.mz_water_min_zoom := mz_calculate_min_zoom_water(NEW.*);
    NEW.mz_places_min_zoom := mz_calculate_min_zoom_places(NEW.*);
    NEW.mz_building_min_zoom := mz_calculate_min_zoom_buildings(NEW.*);
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
    NEW.mz_road_level := mz_calculate_road_level(NEW."highway", NEW."railway", NEW."aeroway", NEW."route", NEW."service", NEW."aerialway", NEW."leisure", NEW."sport", NEW."man_made", NEW."way", NEW."name", NEW."bicycle", NEW."foot", NEW."horse", NEW.tags->'snowmobile', NEW.tags->'ski', NEW.osm_id);
    NEW.mz_transit_level := mz_calculate_min_zoom_transit(NEW.*);
    NEW.mz_water_min_zoom := mz_calculate_min_zoom_water(NEW.*);
    NEW.mz_boundary_min_zoom := mz_calculate_min_zoom_boundaries(NEW.*);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql VOLATILE;

-- do a drop-if-exists + create in a transaction to ensure that the script
-- is idempotent.
BEGIN;
DROP TRIGGER IF EXISTS mz_trigger_line ON planet_osm_line;
CREATE TRIGGER mz_trigger_line BEFORE INSERT OR UPDATE ON planet_osm_line FOR EACH ROW EXECUTE PROCEDURE mz_trigger_function_line();
COMMIT;

CREATE OR REPLACE FUNCTION mz_trigger_function_osm_rels_update()
RETURNS TRIGGER AS $$
DECLARE
  is_old_path_major_route_relation bool := mz_is_path_major_route_relation(hstore(OLD.tags));
  is_new_path_major_route_relation bool := mz_is_path_major_route_relation(hstore(NEW.tags));
  old_way_ids bigint[] := CASE WHEN is_old_path_major_route_relation THEN OLD.parts[OLD.way_off+1:OLD.rel_off] ELSE ARRAY[]::bigint[] END;
  new_way_ids bigint[] := CASE WHEN is_new_path_major_route_relation THEN NEW.parts[NEW.way_off+1:NEW.rel_off] ELSE ARRAY[]::bigint[] END;
BEGIN
  UPDATE planet_osm_line
    SET mz_road_level = mz_calculate_road_level("highway", "railway", "aeroway", "route", "service", "aerialway", "leisure", "sport", "man_made", "way", "name", "bicycle", "foot", "horse", tags->'snowmobile', tags->'ski', osm_id)
    WHERE (array[osm_id] <@ old_way_ids) <> (array[osm_id] <@ new_way_ids);
  RETURN NEW;
END;
$$ LANGUAGE plpgsql VOLATILE;

CREATE OR REPLACE FUNCTION mz_trigger_function_osm_rels_insert()
RETURNS TRIGGER AS $$
DECLARE
  is_new_path_major_route_relation bool := mz_is_path_major_route_relation(hstore(NEW.tags));
  new_way_ids bigint[] := CASE WHEN is_new_path_major_route_relation THEN NEW.parts[NEW.way_off+1:NEW.rel_off] ELSE ARRAY[]::bigint[] END;
BEGIN
  UPDATE planet_osm_line
    SET mz_road_level = mz_calculate_road_level("highway", "railway", "aeroway", "route", "service", "aerialway", "leisure", "sport", "man_made", "way", "name", "bicycle", "foot", "horse", tags->'snowmobile', tags->'ski', osm_id)
    WHERE (array[osm_id] <@ new_way_ids);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql VOLATILE;

CREATE OR REPLACE FUNCTION mz_trigger_function_osm_rels_delete()
RETURNS TRIGGER AS $$
DECLARE
  is_old_path_major_route_relation bool := mz_is_path_major_route_relation(hstore(OLD.tags));
  old_way_ids bigint[] := CASE WHEN is_old_path_major_route_relation THEN OLD.parts[OLD.way_off+1:OLD.rel_off] ELSE ARRAY[]::bigint[] END;
BEGIN
  UPDATE planet_osm_line
    SET mz_road_level = mz_calculate_road_level("highway", "railway", "aeroway", "route", "service", "aerialway", "leisure", "sport", "man_made", "way", "name", "bicycle", "foot", "horse", tags->'snowmobile', tags->'ski', osm_id)
    WHERE (array[osm_id] <@ old_way_ids);
    RETURN NULL;
END;
$$ LANGUAGE plpgsql VOLATILE;

BEGIN;

DROP TRIGGER IF EXISTS mz_trigger_osm_rels_insert ON planet_osm_rels;
CREATE TRIGGER mz_trigger_osm_rels_insert AFTER INSERT ON planet_osm_rels FOR EACH ROW EXECUTE PROCEDURE mz_trigger_function_osm_rels_insert();

DROP TRIGGER IF EXISTS mz_trigger_osm_rels_update ON planet_osm_rels;
CREATE TRIGGER mz_trigger_osm_rels_update AFTER UPDATE ON planet_osm_rels FOR EACH ROW EXECUTE PROCEDURE mz_trigger_function_osm_rels_update();

DROP TRIGGER IF EXISTS mz_trigger_osm_rels_delete ON planet_osm_rels;
CREATE TRIGGER mz_trigger_osm_rels_delete AFTER DELETE ON planet_osm_rels FOR EACH ROW EXECUTE PROCEDURE mz_trigger_function_osm_rels_delete();

COMMIT;
