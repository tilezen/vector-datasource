DROP INDEX IF EXISTS planet_osm_polygon_is_water_index;
DROP FUNCTION IF EXISTS mz_calculate_is_water(text, text, text);

-- drop old versions of the landuse kind / selection functions with fewer
-- arguments than the new versions.
DROP FUNCTION IF EXISTS mz_calculate_landuse_kind(
  text, text, text, text, text, text, text, text, text, text);
DROP FUNCTION IF EXISTS mz_calculate_is_landuse(
  text, text, text, text, text, text, text, text, text, text);

-- drop old version of the POI level calculation function with different
-- arguments (doesn't take tags).
DROP FUNCTION IF EXISTS mz_calculate_poi_level(
  text, text, text, text, text, text, text, text, text, text, text, text, text,
  text, text, text, text, text, real);
