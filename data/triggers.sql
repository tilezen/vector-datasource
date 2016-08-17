CREATE OR REPLACE FUNCTION mz_trigger_function_polygon()
RETURNS TRIGGER AS $$
BEGIN
    NEW.mz_poi_min_zoom := mz_calculate_min_zoom_pois(NEW.*);
    NEW.mz_landuse_min_zoom := mz_calculate_min_zoom_landuse(NEW.*);
    NEW.mz_transit_level := mz_calculate_min_zoom_transit(NEW.*);
    NEW.mz_water_min_zoom := mz_calculate_min_zoom_water(NEW.*);
    NEW.mz_boundary_min_zoom := mz_calculate_min_zoom_boundaries(NEW.*);
    NEW.mz_building_min_zoom := mz_calculate_min_zoom_buildings(NEW.*);
    NEW.mz_earth_min_zoom := mz_calculate_min_zoom_earth(NEW.*);
    NEW.mz_label_placement := ST_PointOnSurface(NEW.way);
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
    NEW.mz_earth_min_zoom := mz_calculate_min_zoom_earth(NEW.*);
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
    NEW.mz_road_level := mz_calculate_min_zoom_roads(NEW.*);
    NEW.mz_transit_level := mz_calculate_min_zoom_transit(NEW.*);
    NEW.mz_water_min_zoom := mz_calculate_min_zoom_water(NEW.*);
    NEW.mz_boundary_min_zoom := mz_calculate_min_zoom_boundaries(NEW.*);
    NEW.mz_landuse_min_zoom := mz_calculate_min_zoom_landuse(NEW.*);
    NEW.mz_earth_min_zoom := mz_calculate_min_zoom_earth(NEW.*);
    NEW.mz_label_placement := ST_PointOnSurface(NEW.way);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql VOLATILE;

-- do a drop-if-exists + create in a transaction to ensure that the script
-- is idempotent.
BEGIN;
DROP TRIGGER IF EXISTS mz_trigger_line ON planet_osm_line;
CREATE TRIGGER mz_trigger_line BEFORE INSERT OR UPDATE ON planet_osm_line FOR EACH ROW EXECUTE PROCEDURE mz_trigger_function_line();
COMMIT;

CREATE OR REPLACE FUNCTION mz_trigger_function_path_major_route_relation_update()
RETURNS TRIGGER AS $$
DECLARE
  is_old_path_major_route_relation bool := mz_is_path_major_route_relation(hstore(OLD.tags));
  is_new_path_major_route_relation bool := mz_is_path_major_route_relation(hstore(NEW.tags));
  old_way_ids bigint[] := CASE WHEN is_old_path_major_route_relation THEN OLD.parts[OLD.way_off+1:OLD.rel_off] ELSE ARRAY[]::bigint[] END;
  new_way_ids bigint[] := CASE WHEN is_new_path_major_route_relation THEN NEW.parts[NEW.way_off+1:NEW.rel_off] ELSE ARRAY[]::bigint[] END;
  all_way_ids bigint[] := array_cat(old_way_ids, new_way_ids);
  way_id bigint;
BEGIN
  FOREACH way_id IN ARRAY all_way_ids LOOP
    INSERT INTO mz_pending_path_major_route (osm_id) VALUES (way_id);
  END LOOP;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql VOLATILE;

CREATE OR REPLACE FUNCTION mz_trigger_function_path_major_route_relation_insert()
RETURNS TRIGGER AS $$
DECLARE
  is_new_path_major_route_relation bool := mz_is_path_major_route_relation(hstore(NEW.tags));
  new_way_ids bigint[] := CASE WHEN is_new_path_major_route_relation THEN NEW.parts[NEW.way_off+1:NEW.rel_off] ELSE ARRAY[]::bigint[] END;
  way_id bigint;
BEGIN
  FOREACH way_id IN ARRAY new_way_ids LOOP
    INSERT INTO mz_pending_path_major_route (osm_id) VALUES (way_id);
  END LOOP;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql VOLATILE;

CREATE OR REPLACE FUNCTION mz_trigger_function_path_major_route_relation_delete()
RETURNS TRIGGER AS $$
DECLARE
  is_old_path_major_route_relation bool := mz_is_path_major_route_relation(hstore(OLD.tags));
  old_way_ids bigint[] := CASE WHEN is_old_path_major_route_relation THEN OLD.parts[OLD.way_off+1:OLD.rel_off] ELSE ARRAY[]::bigint[] END;
  way_id bigint;
BEGIN
  FOREACH way_id IN ARRAY old_way_ids LOOP
    INSERT INTO mz_pending_path_major_route (osm_id) VALUES (way_id);
  END LOOP;
  RETURN NULL;
END;
$$ LANGUAGE plpgsql VOLATILE;

BEGIN;

DROP TRIGGER IF EXISTS mz_trigger_path_major_route_relation_insert ON planet_osm_rels;
CREATE TRIGGER mz_trigger_path_major_route_relation_insert AFTER INSERT ON planet_osm_rels FOR EACH ROW EXECUTE PROCEDURE mz_trigger_function_path_major_route_relation_insert();

DROP TRIGGER IF EXISTS mz_trigger_path_major_route_relation_update ON planet_osm_rels;
CREATE TRIGGER mz_trigger_path_major_route_relation_update AFTER UPDATE ON planet_osm_rels FOR EACH ROW EXECUTE PROCEDURE mz_trigger_function_path_major_route_relation_update();

DROP TRIGGER IF EXISTS mz_trigger_path_major_route_relation_delete ON planet_osm_rels;
CREATE TRIGGER mz_trigger_path_major_route_relation_delete AFTER DELETE ON planet_osm_rels FOR EACH ROW EXECUTE PROCEDURE mz_trigger_function_path_major_route_relation_delete();

COMMIT;
