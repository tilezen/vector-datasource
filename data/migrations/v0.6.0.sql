--
-- drop old versions of functions
--

DROP FUNCTION IF EXISTS mz_calculate_road_level(text, text, text, text, text, text, way geometry);
DROP FUNCTION IF EXISTS mz_calculate_poi_level(text, text, text, text, text, text, text, text, text, text, text, text, text, text, text, text, text, real);
