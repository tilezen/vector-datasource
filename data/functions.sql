CREATE OR REPLACE FUNCTION mz_calculate_ferry_level(way geometry)
RETURNS SMALLINT AS $$
DECLARE
  way_length real := st_length(way);
BEGIN
  RETURN (
    CASE
      -- this is about when the way is >= 2px in length
      WHEN way_length > 1223 THEN  8
      WHEN way_length >  611 THEN  9
      WHEN way_length >  306 THEN 10
      WHEN way_length >  153 THEN 11
      WHEN way_length >   76 THEN 12
      ELSE                        13
    END);
END;
$$ LANGUAGE plpgsql IMMUTABLE;

CREATE OR REPLACE FUNCTION mz_calculate_is_building_or_part(
    building_val text, buildingpart_val text)
RETURNS BOOLEAN AS $$
BEGIN
    -- there are 12,000 uses of building=no, so we ought to take that into
    -- account when figuring out if something is a building or not. also,
    -- returning "kind=no" is a bit weird.
    RETURN ((building_val IS NOT NULL AND building_val <> 'no') OR
            (buildingpart_val IS NOT NULL AND buildingpart_val <> 'no'));
END;
$$ LANGUAGE plpgsql IMMUTABLE;

-- mz_rel_get_tag returns the tag value associated with a given
-- key, or NULL if the tag is not set in the array.
--
-- tags in the planet_osm_rels table are stored in a flat array
-- rather than in an hstore variable. so this function makes it
-- easier to extract values from that array as if it were
-- associative.
--
CREATE OR REPLACE FUNCTION mz_rel_get_tag(
  tags text[],
  k text)
RETURNS text AS $$
DECLARE
  lo CONSTANT integer := array_lower(tags, 1);
  hi CONSTANT integer := array_upper(tags, 1);
BEGIN
  -- if tags is null, then we're not going to find any values
  -- in it, so just short-circuit and return NULL.
  IF tags IS NULL THEN
    RETURN NULL;
  END IF;
  -- tags is an array of key-value pairs inline, so to get the
  -- keys only we want each odd offset.
  FOR i IN 0 .. ((hi - lo - 1) / 2)
  LOOP
    IF tags[2 * i + lo] = k THEN
      RETURN tags[2 * i + lo + 1];
    END IF;
  END LOOP;
  RETURN NULL;
END;
$$ LANGUAGE plpgsql IMMUTABLE;

-- mz_first_dedup returns the lexicographically first non-NULL
-- entry in an array of text.
--
-- this is used to get a single value from the array of perhaps
-- many relations that a way can be a member of. we're not
-- interested in NULL values, so those can be discarded. it
-- remains to be seen if lexicographic ordering is any good for
-- network names, but in the limited testing i've done so far,
-- it seems to do okay.
--
CREATE OR REPLACE FUNCTION mz_first_dedup(
  arr text[])
RETURNS text AS $$
DECLARE
  rv text;
BEGIN
  SELECT DISTINCT y.x INTO rv FROM (SELECT unnest(arr) as x) y
    WHERE y.x IS NOT NULL LIMIT 1;
  RETURN rv;
END;
$$ LANGUAGE plpgsql IMMUTABLE;

-- mz_modify_network returns an hstore of {route, network, ref}
-- where the network has been modified according to the
-- modifier tag, if there is any.
CREATE OR REPLACE FUNCTION mz_modify_network(
  tags hstore)
RETURNS hstore AS $$
DECLARE
  network text := tags->'network';
  modifier text := tags->'modifier';
BEGIN
  RETURN
    tags ||
    hstore('network',
      CASE WHEN
        network LIKE 'US:%' AND
        modifier IN ('Business', 'Spur', 'Truck', 'Alternate', 'Bypass',
                     'Connector', 'Historic', 'Toll', 'Scenic') AND
        POSITION(modifier IN network) = 0
      THEN
        network || ':' || modifier
      ELSE
        network
      END
    );
END;
$$ LANGUAGE plpgsql IMMUTABLE;

-- mz_get_rel_networks returns a list of triples of route type,
-- network and ref tags, or NULL, for a given way ID.
--
-- it does this by joining onto the relations slim table, so it
-- won't work if you dropped the slim tables, or didn't use slim
-- mode in osm2pgsql.
--
CREATE OR REPLACE FUNCTION mz_get_rel_networks(
  way_id bigint)
RETURNS text[] AS $$
SELECT
  array_agg(unnested)
FROM (
  SELECT
    unnest(tags) AS unnested
  FROM (
    SELECT
      mz_modify_network(hstore(tags))->ARRAY['route','network','ref'] AS tags
    FROM
      planet_osm_rels
    WHERE
      parts && ARRAY[way_id] AND
      parts[way_off+1:rel_off] && ARRAY[way_id] AND
      hstore(tags) ? 'route' AND
      (hstore(tags) ? 'network' OR
       hstore(tags) ? 'ref')
    ) inner1
  ) inner2;
$$ LANGUAGE sql STABLE;

-- adds the prefix onto every key in an hstore value
CREATE OR REPLACE FUNCTION mz_hstore_add_prefix(
  tags hstore,
  prefix text)
RETURNS hstore AS $$
DECLARE
  new_tags hstore;
BEGIN
  SELECT hstore(array_agg(prefix || key), array_agg(value))
    INTO STRICT new_tags
    FROM each(tags);
  RETURN new_tags;
END;
$$ LANGUAGE plpgsql IMMUTABLE;

-- OSM tags are often structured as a list separated by ':'s.
-- to preserve some kind of ordering information, we want to
-- insert an element in this "list" after the first element.
-- i.e: mz_insert_one_level('foo:bar', 'x') -> 'foo:x:bar'.
CREATE OR REPLACE FUNCTION mz_insert_one_level(
  tag text,
  str text)
RETURNS text AS $$
DECLARE
  arr text[] = string_to_array(tag, ':');
  fst text   = arr[1];
  len int    = array_upper(arr, 1);
  rst text[] = arr[2:len];
BEGIN
  RETURN array_to_string(ARRAY[fst, str] || rst, ':');
END;
$$ LANGUAGE plpgsql IMMUTABLE;

-- adds an infix value into every key in an hstore value after
-- the first element. so 'foo:bar=>bat' with infix 'x' becomes
-- 'foo:x:bar=>bat'.
CREATE OR REPLACE FUNCTION mz_hstore_add_infix(
  tags hstore,
  infix text)
RETURNS hstore AS $$
DECLARE
  new_tags hstore;
BEGIN
  SELECT hstore(array_agg(mz_insert_one_level(key, infix)), array_agg(value))
    INTO STRICT new_tags
    FROM each(tags);
  RETURN new_tags;
END;
$$ LANGUAGE plpgsql IMMUTABLE;

-- returns the (possibly fractional) zoom at which the given way
-- area will be one square pixel nominally on screen (assuming
-- that tiles are 256x256px at integer zooms). sadly, features
-- aren't always rectangular and axis-aligned, but this should
-- still give a reasonable approximation to the zoom that it
-- would be appropriate to show them.
CREATE OR REPLACE FUNCTION mz_one_pixel_zoom(
  way_area real)
RETURNS real AS $$
BEGIN
  RETURN
    -- can't take logarithm of zero, and some ways have
    -- incredibly tiny areas, down to even zero. also, by z16
    -- all features really should be visible, so we clamp the
    -- computation at the way area which would result in 16
    -- being returned.
    CASE WHEN way_area < 5.704
           THEN 16.0
         ELSE (17.256-ln(way_area)/ln(4))
    END;
END;
$$ LANGUAGE plpgsql IMMUTABLE;

-- for the purposes of sweeping for related public transit features,
-- "interesting" tags are ones which define relations which group public
-- transport features, or group features together in a "site". these are:
--   * public_transport = stop_area
--   * public_transport = stop_area_group
--   * type = stop_area
--   * type = stop_area_group
--   * type = site
--
CREATE OR REPLACE FUNCTION mz_is_interesting_transit_relation(
  tags hstore)
RETURNS BOOLEAN AS $$
BEGIN
  RETURN
    tags->'public_transport' IN ('stop_area', 'stop_area_group') OR
    tags->'type' IN ('stop_area', 'stop_area_group', 'site');
END;
$$ LANGUAGE plpgsql IMMUTABLE;

-- extract a name for a transit route relation. this can expand comma
-- separated lists and prefers to use the ref rather than the name.
CREATE OR REPLACE FUNCTION mz_transit_route_name(
  tags hstore)
RETURNS text AS $$
DECLARE
  route_name text;
BEGIN
  SELECT TRIM(BOTH FROM "name") INTO route_name
    FROM (
      SELECT UNNEST(string_to_array(COALESCE(
        -- prefer ref as it's less likely to contain the destination name
        tags->'ref',
        tags->'name'
      ), ',')) AS "name"
    ) refs_and_names
    LIMIT 1;
  RETURN route_name;
END;
$$ LANGUAGE plpgsql IMMUTABLE;

DO $$
BEGIN

  -- suppress notice message from drop type cascade
  -- we re-add the type immediately afterwards
  SET LOCAL client_min_messages=warning;

  IF EXISTS (SELECT 1 FROM pg_type WHERE typname = 'mz_transit_routes_rettype') THEN
    DROP TYPE mz_transit_routes_rettype CASCADE;
  END IF;

  CREATE TYPE mz_transit_routes_rettype AS (
    -- the "top-most" site or public_transport relation found while exploring
    -- the graph of objects around the station.
    root_relation_id BIGINT,

    -- the "score" of the station. this takes the number of rail routes, the
    -- sum of the number of subway and light rail routes, and the sum of the
    -- number of tram and railway routes. if it is an interchange (i.e: both
    -- rail and subway / light_rail routes) then doubling both those numbers.
    -- these then get maxed out at 9, and turned into a 3-digit number.
    score SMALLINT,

    -- the list of distinct refs (or names if refs aren't present) on each
    -- type of route.
    train_routes      text[],
    subway_routes     text[],
    light_rail_routes text[],
    tram_routes       text[],
    railway_routes    text[]
  );
END$$;

-- examines a point or polygon (by OSM ID) and tries to determine if it is
-- related to a wider set of public transport features, including rail,
-- light rail, subway and tram routes. information about these is returned
-- in the returned type.
--
CREATE OR REPLACE FUNCTION mz_calculate_transit_routes_and_score(
  -- the station OSM ID from the point table, or NULL
  IN station_point_osm_id BIGINT,

  -- the station OSM ID from the polygon table, or NULL. may be negative to
  -- indicate a relation.
  IN station_polygon_osm_id BIGINT,

  -- the returned data - see the type definition for details.
  OUT retval mz_transit_routes_rettype)
AS $$
DECLARE
  -- the IDs of a "seed" set of relations which directly include any
  -- station node, way or relation passed as input.
  seed_relations bigint[];

  -- IDs of nodes which are tagged as stations or stops and are
  -- members of the stop area relations. these will contain the
  -- original `station_node_id`, but probably many others as well.
  stations_and_stops bigint[];

  -- IDs of ways which contain any of the stations and stops.
  -- these are included because sometimes the stop node isn't
  -- directly included in the route relation, only the way
  -- representing the track itself. this also contains the original
  -- `station_way_id` in case it's directly included in any routes.
  stations_and_lines bigint[];

  -- all the relation IDs as an array for intersecting with the
  -- "parts" array in planet_osm_rels.
  all_rel_ids bigint[];

  -- all the IDs of everything to intersect with the "parts" of
  -- planet_osm_rels when looking for route relations.
  all_interesting_ids bigint[];

  -- the IDs of all the route relations found
  all_routes bigint[];

  -- number of each type of route.
  num_train_routes smallint;
  num_subway_routes smallint;
  num_light_rail_routes smallint;
  num_tram_routes smallint;
  num_railway_routes smallint;

  -- a 'bonus' is given to the score of stations which are interchanges
  -- between mainline railway and subway or light rail.
  bonus smallint;

BEGIN
  -- find any "interesting" relations which contain the given station
  -- features as members.
  seed_relations := ARRAY(
    SELECT id
    FROM planet_osm_rels
    WHERE
      (ARRAY[station_point_osm_id, station_polygon_osm_id,
             -station_polygon_osm_id] && parts) AND
      (ARRAY[station_point_osm_id] && parts[1:way_off] OR
       ARRAY[station_polygon_osm_id] && parts[way_off+1:rel_off] OR
       ARRAY[-station_polygon_osm_id] && parts[rel_off+1:array_upper(parts,1)]) AND
      mz_is_interesting_transit_relation(hstore(tags))
    UNION
    -- manually include the station multipolygon relation so that we can
    -- sweep down its members too.
    SELECT -station_polygon_osm_id AS id WHERE station_polygon_osm_id < 0
    );

  -- this complex query does two recursive sweeps of the relations
  -- table starting from a seed set of relations which are or contain
  -- the original station.
  --
  -- the first sweep goes "upwards" from relations to "parent" relations. if
  -- a relation R1 is a member of relation R2, then R2 will be included in
  -- this sweep as long as it has "interesting" tags, as defined by the
  -- function mz_is_interesting_transit_relation.
  --
  -- the second sweep goes "downwards" from relations to "child" relations.
  -- if a relation R1 has a member R2 which is also a relation, then R2 will
  -- be included in this sweep as long as it also has "interesting" tags.
  --
  all_rel_ids := ARRAY(
    WITH RECURSIVE upward_search(level,path,id,parts,rel_off,cycle) AS (
        SELECT 0,ARRAY[id],id,parts,rel_off,false
        FROM planet_osm_rels WHERE id = ANY(seed_relations)
      UNION
        SELECT
          level + 1,
          path || r.id,
          r.id,
          r.parts,
          r.rel_off,
          r.id = ANY(path)
        FROM
          planet_osm_rels r JOIN upward_search s
        ON
          ARRAY[s.id] && r.parts
        WHERE
          ARRAY[s.id] && r.parts[r.rel_off+1:array_upper(r.parts,1)] AND
          mz_is_interesting_transit_relation(hstore(r.tags)) AND
          NOT cycle
      )
    SELECT id FROM upward_search ORDER BY level DESC);

  IF array_upper(all_rel_ids, 1) > 0 THEN
    retval.root_relation_id := all_rel_ids[1];
  ELSE
    retval.root_relation_id := NULL;
  END IF;

  all_rel_ids := ARRAY(
    WITH RECURSIVE downward_search(path,id,parts,rel_off,cycle) AS (
        SELECT ARRAY[id],id,parts,rel_off,false
        FROM planet_osm_rels WHERE id = ANY(all_rel_ids)
      UNION
        SELECT
          path || r.id,
          r.id,
          r.parts,
          r.rel_off,
          r.id = ANY(path)
        FROM
          planet_osm_rels r JOIN downward_search s
        ON
          r.id = ANY(s.parts[s.rel_off+1:array_upper(s.parts,1)])
        WHERE
          mz_is_interesting_transit_relation(hstore(r.tags)) AND
          NOT cycle
    ) SELECT id FROM downward_search WHERE NOT cycle);

  -- collect all the interesting nodes - this includes the station node (if
  -- any) and any nodes which are members of found relations which have
  -- public transport tags indicating that they're stations or stops.
  stations_and_stops := ARRAY(
    SELECT DISTINCT id
    FROM
      (SELECT UNNEST(parts[1:way_off]) AS id
       FROM planet_osm_rels
       WHERE id = ANY(all_rel_ids)) n
    JOIN planet_osm_point p
    ON n.id = p.osm_id
    WHERE
      (p.tags->'railway' IN ('station', 'stop', 'tram_stop') OR
       p.tags->'public_transport' IN ('stop', 'stop_position', 'tram_stop'))
    -- re-include the station node, if there was one.
    UNION
    SELECT station_point_osm_id AS id
    WHERE station_point_osm_id IS NOT NULL);

  -- collect any physical railway which includes any of the above
  -- nodes.
  stations_and_lines := ARRAY(
    SELECT DISTINCT w.id
    FROM planet_osm_ways w
    WHERE w.nodes && stations_and_stops
    AND hstore(w.tags)->'railway' IN ('subway', 'light_rail', 'tram', 'rail')
    -- manually re-include the original station way, in case it's
    -- not part of a public_transport=stop_area relation.
    UNION SELECT station_polygon_osm_id AS id
    WHERE station_polygon_osm_id > 0
  );

  -- collect all IDs together in one array to intersect with the parts arrays
  -- of route relations which may include them.
  all_interesting_ids = stations_and_stops || stations_and_lines || all_rel_ids;

  all_routes := ARRAY(
    SELECT DISTINCT id
    FROM planet_osm_rels
    WHERE
      parts && all_interesting_ids AND
      (parts[1:way_off] && stations_and_stops OR
       parts[way_off+1:rel_off] && stations_and_lines OR
       parts[rel_off+1:array_upper(parts,1)] && all_rel_ids) AND
      hstore(tags)->'type' = 'route' AND
      hstore(tags)->'route' IN ('subway', 'light_rail', 'tram', 'train',
        'railway'));

  -- extract the route ref/name for routes
  retval.train_routes := ARRAY(
    SELECT DISTINCT mz_transit_route_name(hstore(tags)) FROM planet_osm_rels
    WHERE id = ANY(all_routes) AND hstore(tags)->'route' = 'train');

  retval.subway_routes := ARRAY(
    SELECT DISTINCT mz_transit_route_name(hstore(tags)) FROM planet_osm_rels
    WHERE id = ANY(all_routes) AND hstore(tags)->'route' = 'subway');

  retval.light_rail_routes := ARRAY(
    SELECT DISTINCT mz_transit_route_name(hstore(tags)) FROM planet_osm_rels
    WHERE id = ANY(all_routes) AND hstore(tags)->'route' = 'light_rail');

  retval.tram_routes := ARRAY(
    SELECT DISTINCT mz_transit_route_name(hstore(tags)) FROM planet_osm_rels
    WHERE id = ANY(all_routes) AND hstore(tags)->'route' = 'tram');

  retval.railway_routes := ARRAY(
    SELECT DISTINCT mz_transit_route_name(hstore(tags)) FROM planet_osm_rels
    WHERE id = ANY(all_routes) AND hstore(tags)->'route' = 'railway');

  -- calculate a score between 0 and 999 for stations.
  num_train_routes := COALESCE(array_upper(retval.train_routes, 1), 0);
  num_subway_routes := COALESCE(array_upper(retval.subway_routes, 1), 0);
  num_light_rail_routes := COALESCE(array_upper(retval.light_rail_routes, 1), 0);
  num_tram_routes := COALESCE(array_upper(retval.tram_routes, 1), 0);
  num_railway_routes := COALESCE(array_upper(retval.railway_routes, 1), 0);

  -- if a station is an interchange between mainline rail and subway or light
  -- rail, then give it a "bonus" boost of importance.
  IF num_train_routes > 0 AND
    (num_subway_routes + num_light_rail_routes) > 0 THEN
    bonus := 2;
  ELSE
    bonus := 1;
  END IF;

  retval.score :=
    100 * LEAST(9, bonus * num_train_routes) +
    10 * LEAST(9, bonus * (num_subway_routes + num_light_rail_routes)) +
    LEAST(9, num_tram_routes + num_railway_routes);
END;
$$ LANGUAGE plpgsql STABLE;

-- returns true if the text is numeric and can be cast
-- to a float without error.
CREATE OR REPLACE FUNCTION mz_is_numeric(
  t text)
RETURNS BOOLEAN AS $$
BEGIN
  RETURN t ~ '^([0-9]+[.]?[0-9]*|[.][0-9]+)$';
END;
$$ LANGUAGE plpgsql IMMUTABLE;

-- Calculate the height of a building by looking at either the
-- height tag, if one is set explicitly, or by calculating the
-- approximate height from the number of levels, if that is
-- set.
CREATE OR REPLACE FUNCTION mz_building_height(
  height text, levels text)
RETURNS REAL AS $$
BEGIN
  RETURN CASE
    -- if height is present, and can be parsed as a
    -- float, then we can filter right here.
    WHEN mz_is_numeric(height) THEN
      height::float

    -- looks like we assume each level is 3m, plus
    -- 2 overall.
    WHEN mz_is_numeric("levels") THEN
      (GREATEST(levels::float, 1) * 3 + 2)

    -- if height is present, but not numeric, then
    -- we have no idea what it could be, and we must
    -- assume it could be very large.
    WHEN "height" IS NOT NULL OR "levels" IS NOT NULL THEN
      1.0e10
    ELSE NULL END;
END;
$$ LANGUAGE plpgsql IMMUTABLE;

-- Update the wof_neighbourhood table so that the `is_visible` field
-- is correct as of the given date `d`. The function returns the set
-- of WOF IDs which have been updated, and the locations of which
-- should be expired.
CREATE OR REPLACE FUNCTION wof_update_visible_ids(
  d DATE)
RETURNS SETOF BIGINT AS $$
UPDATE wof_neighbourhood a
  SET is_visible = b.new_visible
  FROM (
    SELECT wof_id, inception < d AND cessation >= d AS new_visible
    FROM wof_neighbourhood
  ) b
  WHERE
    a.wof_id = b.wof_id AND
    b.new_visible <> a.is_visible
  RETURNING a.wof_id;
$$ LANGUAGE sql VOLATILE;

-- returns TRUE if the given way ID (osm_id) is part of a bus route relation,
-- or NULL otherwise.
CREATE OR REPLACE FUNCTION mz_calculate_is_bus_route(osm_id BIGINT)
RETURNS BOOLEAN AS $$
BEGIN
  IF EXISTS(
    SELECT 1 FROM planet_osm_rels
    WHERE
      parts && ARRAY[osm_id] AND
      parts[way_off+1:rel_off] && ARRAY[osm_id] AND
      hstore(tags)->'type' = 'route' AND
      hstore(tags)->'route' IN ('bus', 'trolleybus')) THEN
    RETURN TRUE;
  END IF;
  RETURN NULL;
END;
$$ LANGUAGE plpgsql STABLE;

CREATE OR REPLACE FUNCTION mz_is_path_major_route_relation(tags hstore)
RETURNS BOOLEAN AS $$
BEGIN
    RETURN (
      tags->'type' = 'route' AND
      tags->'route' IN ('hiking', 'foot', 'bicycle') AND
      tags->'network' IN ('iwn','nwn','rwn','lwn','icn','ncn','rcn','lcn')
    );
END;
$$ LANGUAGE plpgsql IMMUTABLE;

-- Looks up whether the given osm_id is a member of any hiking routes
-- and, if so, returns the network designation of the most important
-- (highest in hierarchy) of the networks.
--
CREATE OR REPLACE FUNCTION mz_hiking_network(osm_id bigint)
RETURNS text AS $$
DECLARE
  networks text[] := ARRAY(
    SELECT hstore(tags)->'network'
    FROM planet_osm_rels
    WHERE parts && ARRAY[osm_id]
      AND parts[way_off+1:rel_off] && ARRAY[osm_id]
      AND mz_is_path_major_route_relation(hstore(tags)));
BEGIN
  RETURN CASE
    WHEN networks && ARRAY['iwn'] THEN 'iwn'
    WHEN networks && ARRAY['nwn'] THEN 'nwn'
    WHEN networks && ARRAY['rwn'] THEN 'rwn'
    WHEN networks && ARRAY['lwn'] THEN 'lwn'
  END;
END;
$$ LANGUAGE plpgsql STABLE;

CREATE OR REPLACE FUNCTION mz_cycling_network_(way_tags hstore, osm_id bigint)
RETURNS text AS $$
DECLARE
  networks text[] := ARRAY(
    SELECT hstore(tags)->'network'
    FROM planet_osm_rels
    WHERE parts && ARRAY[osm_id]
      AND parts[way_off+1:rel_off] && ARRAY[osm_id]
      AND mz_is_path_major_route_relation(hstore(tags)));
BEGIN
  RETURN CASE
    WHEN networks && ARRAY['icn'] THEN 'icn'
    WHEN networks && ARRAY['ncn'] THEN 'ncn'
    WHEN way_tags->'ncn'='yes' OR way_tags ? 'ncn_ref' THEN 'ncn'
    WHEN networks && ARRAY['rcn'] THEN 'rcn'
    WHEN way_tags->'rcn'='yes' OR way_tags ? 'rcn_ref' THEN 'rcn'
    WHEN networks && ARRAY['lcn'] THEN 'lcn'
    WHEN way_tags->'lcn'='yes' OR way_tags ? 'lcn_ref' THEN 'lcn'
  END;
END;
$$ LANGUAGE plpgsql STABLE;

CREATE OR REPLACE FUNCTION mz_cycling_network(way_tags hstore, osm_id bigint)
RETURNS text AS $$
BEGIN
  RETURN CASE
    WHEN way_tags->'icn' = 'yes' OR way_tags ? 'icn_ref' THEN 'icn'
    ELSE mz_cycling_network_(way_tags, osm_id)
  END;
END;
$$ LANGUAGE plpgsql STABLE;

-- returns TRUE if the given way ID (osm_id) is part of a path route relation,
-- or NULL otherwise.
-- This function is meant to be called for something that we already know is a path.
-- Please ensure input is already a path, or output will be undefined.
--
-- Note that the dummy argument is just there to make the "shape" of the
-- arguments the same as with Python, where we need to pass in the relation
-- information rather than query it from `planet_osm_rels`.
CREATE OR REPLACE FUNCTION mz_calculate_path_major_route(osm_id BIGINT, dummy INTEGER)
RETURNS SMALLINT AS $$
BEGIN
  RETURN (
    SELECT
        MIN(
            CASE WHEN hstore(tags)->'network' IN ('icn', 'ncn') THEN 8
                 WHEN hstore(tags)->'network' IN ('iwn', 'nwn') THEN 9
                 WHEN hstore(tags)->'network' IN ('rcn') THEN 10
                 WHEN hstore(tags)->'network' IN ('rwn') THEN 11
                 WHEN hstore(tags)->'network' IN ('lcn') THEN 11
                 WHEN hstore(tags)->'network' IN ('lwn') THEN 12
            ELSE NULL
            END
        )
        AS p
     FROM planet_osm_rels
    WHERE
      parts && ARRAY[osm_id] AND
      parts[way_off+1:rel_off] && ARRAY[osm_id] AND
      mz_is_path_major_route_relation(hstore(tags))
  );
END;
$$ LANGUAGE plpgsql STABLE;

-- Returns a floating point number in meters for the given unit input text,
-- which must be of the form of a number (in which case it's assumed it's
-- meters), or a number followed by a unit (m, ft, '). The distance is
-- converted into meters and returned, or NULL is returned if the input
-- could not be understood.
--
CREATE OR REPLACE FUNCTION mz_to_float_meters(txt text)
RETURNS REAL AS $$
DECLARE
  decimal_matches text[] :=
    regexp_matches(txt, '([0-9]+(\.[0-9]*)?) *(mi|km|m|nmi|ft)');
  imperial_matches text[] :=
    regexp_matches(txt, E'([0-9]+(\\.[0-9]*)?)\x27 *(([0-9]+)")?');
  numeric_matches text[] :=
    regexp_matches(txt, '([0-9]+(\.[0-9]*)?)');
BEGIN
  RETURN CASE
    WHEN decimal_matches IS NOT NULL THEN
      CASE
        WHEN decimal_matches[3] = 'mi'  THEN 1609.3440 * decimal_matches[1]::real
        WHEN decimal_matches[3] = 'km'  THEN 1000.0000 * decimal_matches[1]::real
        WHEN decimal_matches[3] = 'm'   THEN    1.0000 * decimal_matches[1]::real
        WHEN decimal_matches[3] = 'nmi' THEN 1852.0000 * decimal_matches[1]::real
        WHEN decimal_matches[3] = 'ft'  THEN    0.3048 * decimal_matches[1]::real
      END
    WHEN imperial_matches IS NOT NULL THEN
      CASE WHEN imperial_matches[4] IS NULL THEN
        0.0254 * (imperial_matches[1]::real * 12)
      ELSE
        0.0254 * (imperial_matches[1]::real * 12 + imperial_matches[4]::real)
      END
    WHEN numeric_matches IS NOT NULL THEN
      numeric_matches[1]::real
    END;
END;
$$ LANGUAGE plpgsql IMMUTABLE;

CREATE OR REPLACE FUNCTION mz_to_json_null_safe(val anyelement)
RETURNS JSON AS $$
DECLARE
BEGIN
  RETURN CASE WHEN val IS NULL THEN 'null' ELSE to_json(val) END;
END;
$$ LANGUAGE plpgsql IMMUTABLE;

CREATE OR REPLACE FUNCTION mz_building_kind_detail(val TEXT)
RETURNS TEXT AS $$
DECLARE
BEGIN
  RETURN CASE WHEN val IN (
                  'bangunan',
                  'building',
                  'other',
                  'rumah',
                  'Rumah',
                  'Rumah Masyarakat',
                  'rumah_penduduk',
                  'true',
                  'trullo',
                  'yes'
              ) THEN NULL
              WHEN val IN (
                  'abandoned',
                  'administrative',
                  'agricultural',
                  'airport',
                  'allotment_house',
                  'apartments',
                  'arbour',
                  'bank',
                  'barn',
                  'basilica',
                  'beach_hut',
                  'bell_tower',
                  'boathouse',
                  'brewery',
                  'bridge',
                  'bungalow',
                  'bunker',
                  'cabin',
                  'carport',
                  'castle',
                  'cathedral',
                  'chapel',
                  'chimney',
                  'church',
                  'civic',
                  'clinic',
                  'clubhouse',
                  'collapsed',
                  'college',
                  'commercial',
                  'construction',
                  'container',
                  'convent',
                  'cowshed',
                  'dam',
                  'damaged',
                  'depot',
                  'destroyed',
                  'detached',
                  'disused',
                  'dormitory',
                  'duplex',
                  'factory',
                  'farm',
                  'farm_auxiliary',
                  'fire_station',
                  'garage',
                  'garages',
                  'gazebo',
                  'ger',
                  'glasshouse',
                  'government',
                  'grandstand',
                  'greenhouse',
                  'hangar',
                  'healthcare',
                  'hermitage',
                  'hospital',
                  'hotel',
                  'house',
                  'houseboat',
                  'hut',
                  'industrial',
                  'kindergarten',
                  'kiosk',
                  'library',
                  'mall',
                  'manor',
                  'manufacture',
                  'mobile_home',
                  'monastery',
                  'mortuary',
                  'mosque',
                  'museum',
                  'office',
                  'outbuilding',
                  'parking',
                  'pavilion',
                  'power',
                  'prison',
                  'proposed',
                  'pub',
                  'public',
                  'residential',
                  'restaurant',
                  'retail',
                  'roof',
                  'ruin',
                  'ruins',
                  'school',
                  'semidetached_house',
                  'service',
                  'shed',
                  'shelter',
                  'shop',
                  'shrine',
                  'silo',
                  'slurry_tank',
                  'stable',
                  'stadium',
                  'static_caravan',
                  'storage',
                  'storage_tank',
                  'store',
                  'substation',
                  'summer_cottage',
                  'summer_house',
                  'supermarket',
                  'synagogue',
                  'tank',
                  'temple',
                  'terrace',
                  'tower',
                  'train_station',
                  'transformer_tower',
                  'transportation',
                  'university',
                  'utility',
                  'veranda',
                  'warehouse',
                  'wayside_shrine',
                  'works'
              ) THEN val
              WHEN val = 'barne' THEN 'barn'
              WHEN val = 'commercial;residential' THEN 'mixed_use'
              WHEN val = 'constructie' THEN 'construction'
              WHEN val = 'dwelling_house' THEN 'house'
              WHEN val = 'education' THEN 'school'
              WHEN val = 'greenhouse_horticulture' THEN 'greenhouse'
              WHEN val IN ('apartment', 'flat') THEN 'apartments'
              WHEN val IN ('houses', 'residences', 'residence', 'perumahan permukiman', 'residentiel1') THEN 'residential'
              WHEN val IN ('semi_detached', 'semi-detached', 'semi') THEN 'semidetached_house'
              WHEN val = 'offices' THEN 'office'
              WHEN val = 'prefab_container' THEN 'container'
              WHEN val = 'public_building' THEN 'public'
              WHEN val = 'railway_station' THEN 'train_station'
              WHEN val = 'roof=permanent' THEN 'roof'
              WHEN val = 'stables' THEN 'stable'
              WHEN val = 'static caravan' THEN 'static_caravan'
              WHEN val = 'station' THEN 'transportation'
              WHEN val = 'storage tank' THEN 'storage_tank'
              WHEN val = 'townhome' THEN 'terrace'
              ELSE NULL END;
END;
$$ LANGUAGE plpgsql IMMUTABLE;

CREATE OR REPLACE FUNCTION mz_building_part_kind_detail(val TEXT)
RETURNS TEXT AS $$
DECLARE
BEGIN
  RETURN CASE WHEN val IN ('yes', 'part', 'church:part', 'default') THEN NULL
              WHEN val IN (
                'arch',
                'balcony',
                'base',
                'column',
                'door',
                'elevator',
                'entrance',
                'floor',
                'hall',
                'main',
                'passageway',
                'pillar',
                'porch',
                'ramp',
                'roof',
                'room',
                'steps',
                'stilobate',
                'tier',
                'tower',
                'verticalpassage',
                'wall',
                'window'
              ) THEN val
              WHEN val IN ('corridor', 'Corridor', 'vertical', 'verticalpassage') THEN 'verticalpassage'
              WHEN val IN ('stairs', 'stairway') THEN 'steps'
              ELSE NULL END;
END;
$$ LANGUAGE plpgsql IMMUTABLE;

--- Identifies and returns the min_zoom for gates
--- given the highway level of gate location
-- NOTE: the dummy integer is just to make the "shape" of the arguments the same
-- between SQL and Python, since the latter needs to be passed ways which
-- SQL just looks up in the `planet_osm_ways` table.
CREATE OR REPLACE FUNCTION mz_get_min_zoom_highway_level_gate(val_osm_id BIGINT, dummy INTEGER)
RETURNS SMALLINT AS $$
BEGIN
  RETURN MAX(CASE
    WHEN highway IN ('motorway', 'trunk', 'primary', 'motorway_link',
                     'trunk_link', 'primary_link') THEN 14
    WHEN highway IN ('secondary', 'tertiary', 'secondary_link',
                     'tertiary_link') THEN 15
    WHEN highway IN ('residential', 'service', 'path', 'track', 'footway', 'unclassified') THEN 16
    ELSE 17
  END) AS highway_level FROM (
  SELECT
  p.osm_id,
  hstore(w.tags)->'highway' AS highway
  FROM planet_osm_point p
  JOIN planet_osm_ways w
  ON ARRAY[p.osm_id] && w.nodes
  WHERE
      p.osm_id = val_osm_id
    ) x
        GROUP BY osm_id;
END;
$$ LANGUAGE plpgsql STABLE;

-- calculates the building height given the footprint area and the tags, which
-- provide either the height or the number of levels to approximate the height.
CREATE OR REPLACE FUNCTION mz_calculate_building_volume(way_area REAL, tags hstore)
RETURNS REAL AS $$
BEGIN
  RETURN mz_building_height(tags->'height', tags->'building:levels') * way_area;
END
$$ LANGUAGE plpgsql IMMUTABLE;

-- removes the leading 'SH' in the label text.
-- this is used for removing that prefix from the refs of New Zealand highways
-- (perhaps SH = State Highway?) because we put the 'SH' as part of the network
-- and want to keep a numeric ref.
CREATE OR REPLACE FUNCTION trim_nz_sh(label TEXT)
RETURNS TEXT AS $$
BEGIN
  RETURN trim(leading 'SH' from label);
END
$$ LANGUAGE plpgsql IMMUTABLE;

-- returns a JSONB object containing __ne_min_zoom and __ne_max_zoom set to the
-- label min and max zoom of any matching row from the Natural Earth countries,
-- map units and states/provinces themes.
CREATE OR REPLACE FUNCTION tz_get_ne_min_max_zoom(wikidata_id TEXT)
RETURNS JSONB AS $$
DECLARE
  min_zoom REAL;
  max_zoom REAL;
BEGIN
  IF wikidata_id IS NULL THEN
    RETURN '{}'::jsonb;
  END IF;

  -- first, try the countries table
  SELECT
    min_label, max_label INTO min_zoom, max_zoom
    FROM ne_10m_admin_0_countries c
    WHERE c.wikidataid = wikidata_id;

  -- if that fails, try map_units (which contains some sub-country but super-
  -- state level stuff such as England, Scotland and Wales).
  IF NOT FOUND THEN
    SELECT
      min_label, max_label INTO min_zoom, max_zoom
      FROM ne_10m_admin_0_map_units mu
      WHERE mu.wikidataid = wikidata_id;
  END IF;

  -- finally, try states and provinces
  IF NOT FOUND THEN
    SELECT
      min_label, max_label INTO min_zoom, max_zoom
      FROM ne_10m_admin_1_states_provinces sp
      WHERE sp.wikidataid = wikidata_id;
  END IF;

  -- return an empty JSONB rather than null, so that it can be safely
  -- concatenated with whatever other JSONB rather than needing a check for
  -- null.
  IF NOT FOUND THEN
    RETURN '{}'::jsonb;
  END IF;
  RETURN jsonb_build_object(
    '__ne_min_zoom', min_zoom,
    '__ne_max_zoom', max_zoom
  );
END
$$ LANGUAGE plpgsql STABLE;

-- return the min zoom for a node that looks like a service area.
CREATE OR REPLACE FUNCTION tz_looks_like_service_area(name TEXT)
RETURNS INTEGER AS $$
BEGIN
  IF name ILIKE '%service area' OR name ILIKE '%services' OR name ILIKE '%travel plaza' THEN
    RETURN 13;
  END IF;
  RETURN 17;
END;
$$ LANGUAGE plpgsql IMMUTABLE;

-- return the min zoom for a node that looks like a rest area.
CREATE OR REPLACE FUNCTION tz_looks_like_rest_area(name TEXT)
RETURNS INTEGER AS $$
BEGIN
  IF name ILIKE '%rest area' THEN
    RETURN 13;
  END IF;
  RETURN 17;
END;
$$ LANGUAGE plpgsql IMMUTABLE;

-- return the capacity of a parking lot, or estimate it from the area and building levels.
CREATE OR REPLACE FUNCTION tz_estimate_parking_capacity(capacity TEXT, parking TEXT, levels TEXT, way_area REAL)
RETURNS INTEGER AS $$
DECLARE
  levels_int INTEGER;
  spaces_per_level INTEGER;
BEGIN
  -- if the capacity is set, then use that.
  IF capacity ~ '^[0-9]+$' THEN
    RETURN capacity::integer;
  END IF;
  -- otherwise, try to use the information we have to guess the capacity
  spaces_per_level := (way_area / 46.0)::integer;
  levels_int := CASE
    WHEN levels ~ '^[0-9]+$' THEN levels::integer
    WHEN parking = 'multi-storey' THEN 2
    ELSE 1
  END;
  -- if we get a silly answer, don't set that - just return NULL to indicate
  -- that we're unsure.
  IF levels_int * spaces_per_level > 0 THEN
    RETURN levels_int * spaces_per_level;
  ELSE
    RETURN NULL;
  END IF;
END;
$$ LANGUAGE plpgsql IMMUTABLE;

-- try to convert a string into an integer, returning null if that fails.
CREATE OR REPLACE FUNCTION tz_safe_int(t text)
RETURNS INTEGER AS $$
DECLARE
  val INTEGER DEFAULT NULL;
BEGIN
  BEGIN
    val := (t)::INTEGER;
  EXCEPTION WHEN OTHERS THEN
    RETURN NULL;
  END;
  RETURN val;
END;
$$ LANGUAGE plpgsql IMMUTABLE;

-- get extra wikidata properties matched to an OSM feature on the wikidata ID
CREATE OR REPLACE FUNCTION extra_wikidata_properties(wikidata_id text)
RETURNS JSONB AS $$
DECLARE
  tags HSTORE DEFAULT NULL;
  ne_tags HSTORE DEFAULT NULL;
BEGIN
  IF wikidata_id IS NOT NULL THEN
    SELECT w.tags INTO tags FROM wikidata w WHERE w.id = wikidata_id;
    SELECT hstore(ARRAY[
      'featurecla', ne_pp.featurecla,
      'fclass_iso', ne_pp.fclass_iso,
      'fclass_ar', ne_pp.fclass_ar,
      'fclass_bd', ne_pp.fclass_bd,
      'fclass_br', ne_pp.fclass_br,
      'fclass_cn', ne_pp.fclass_cn,
      'fclass_de', ne_pp.fclass_de,
      'fclass_eg', ne_pp.fclass_eg,
      'fclass_es', ne_pp.fclass_es,
      'fclass_fr', ne_pp.fclass_fr,
      'fclass_gb', ne_pp.fclass_gb,
      'fclass_gr', ne_pp.fclass_gr,
      'fclass_id', ne_pp.fclass_id,
      'fclass_il', ne_pp.fclass_il,
      'fclass_in', ne_pp.fclass_in,
      'fclass_it', ne_pp.fclass_it,
      'fclass_jp', ne_pp.fclass_jp,
      'fclass_ko', ne_pp.fclass_ko,
      'fclass_ma', ne_pp.fclass_ma,
      'fclass_nl', ne_pp.fclass_nl,
      'fclass_np', ne_pp.fclass_np,
      'fclass_pk', ne_pp.fclass_pk,
      'fclass_pl', ne_pp.fclass_pl,
      'fclass_ps', ne_pp.fclass_ps,
      'fclass_pt', ne_pp.fclass_pt,
      'fclass_ru', ne_pp.fclass_ru,
      'fclass_sa', ne_pp.fclass_sa,
      'fclass_se', ne_pp.fclass_se,
      'fclass_tr', ne_pp.fclass_tr,
      'fclass_tw', ne_pp.fclass_tw,
      'fclass_us', ne_pp.fclass_us,
      'fclass_vn', ne_pp.fclass_vn
    ]) INTO ne_tags FROM ne_10m_populated_places ne_pp
    WHERE ne_pp.wikidataid = wikidata_id;
  END IF;
  RETURN to_jsonb(coalesce(tags, ''::hstore) || coalesce(ne_tags, ''::hstore));
END;
$$ LANGUAGE plpgsql STABLE;
