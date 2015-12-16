DO $$
BEGIN

IF NOT EXISTS (
  SELECT 1
  FROM   pg_class c
  JOIN   pg_namespace n ON n.oid = c.relnamespace
  WHERE  c.relname = 'planet_osm_line_piste_geom_index'
  AND    n.nspname = 'public'
  ) THEN

  CREATE INDEX planet_osm_line_piste_geom_index ON planet_osm_line USING gist(way) WHERE tags ? 'piste:type';
END IF;

END$$;
DO $$
BEGIN

IF NOT EXISTS (
  SELECT 1
  FROM   pg_class c
  JOIN   pg_namespace n ON n.oid = c.relnamespace
  WHERE  c.relname = 'planet_osm_line_railway_platform_index'
  AND    n.nspname = 'public'
  ) THEN

  CREATE INDEX planet_osm_line_railway_platform_index ON planet_osm_line USING gist(way) WHERE railway='platform';
END IF;

END$$;

UPDATE planet_osm_line
  SET mz_road_level = mz_calculate_road_level(highway, railway, aeroway, route, service, aerialway, leisure, sport, man_made, way)
WHERE man_made IN ('snow_fence', 'pier')
   OR (leisure = 'track'
     AND sport IN ('athletics', 'running', 'horse_racing', 'bmx', 'disc_golf',
       'cycling', 'ski_jumping', 'motor', 'karting', 'obstacle_course',
       'equestrian', 'alpine_slide', 'soap_box_derby', 'mud_truck_racing',
       'skiing', 'drag_racing', 'archery'));
