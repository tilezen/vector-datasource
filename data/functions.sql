-- IF YOU UPDATE THIS, PLEASE UPDATE mz_calculate_landuse_kind
-- BELOW!
CREATE OR REPLACE FUNCTION mz_calculate_is_landuse(
    landuse_val text, leisure_val text, natural_val text, highway_val text,
    amenity_val text, aeroway_val text, tourism_val text, man_made_val text,
    power_val text, boundary_val text)
RETURNS BOOLEAN AS $$
BEGIN
    RETURN
        landuse_val IN ('park', 'forest', 'residential', 'retail', 'commercial',
                        'industrial', 'railway', 'cemetery', 'grass', 'farmyard',
                        'farm', 'farmland', 'wood', 'meadow', 'village_green',
                        'recreation_ground', 'allotments', 'quarry', 'urban', 'rural'
                        'military')
     OR leisure_val IN ('park', 'garden', 'playground', 'golf_course', 'sports_centre',
                        'pitch', 'stadium', 'common', 'nature_reserve')
     OR natural_val IN ('wood', 'land', 'scrub', 'wetland', 'glacier', 'beach')
     OR highway_val IN ('pedestrian', 'footway')
     OR amenity_val IN ('university', 'school', 'college', 'library', 'fuel',
                        'parking', 'cinema', 'theatre', 'place_of_worship', 'hospital')
     OR aeroway_val IN ('runway', 'taxiway', 'apron', 'aerodrome')
     OR tourism_val IN ('zoo')
     OR man_made_val IN ('pier', 'wastewater_plant', 'works', 'bridge', 'tower',
                         'breakwater', 'water_works', 'groyne', 'dike', 'cutline')
     OR power_val IN   ('plant', 'generator', 'substation', 'station', 'sub_station')
     OR boundary_val IN ('national_park', 'protected_area');
END;
$$ LANGUAGE plpgsql IMMUTABLE;

-- calculate the collapse of several properties onto one string
-- 'kind'. this involves a series of precedence choices, as
-- it's possible for a feature to have values in several of
-- these categories. in general, the "most important" should go
-- first, or its presence should modify the later.
--
-- IF YOU UPDATE THIS, PLEASE UPDATE mz_calculate_is_landuse
-- ABOVE!
CREATE OR REPLACE FUNCTION mz_calculate_landuse_kind(
  landuse_val text,
  leisure_val text,
  natural_val text,
  highway_val text,
  aeroway_val text,
  amenity_val text,
  tourism_val text,
  man_made_val text,
  power_val text,
  boundary_val text)
RETURNS text AS $$
BEGIN
  RETURN
    CASE
      WHEN boundary_val IN (
        'national_park', 'protected_area')
	THEN boundary_val
      -- promote this above landuse as it's more specific, and we
      -- don't want to lump nature reserves in with all of the
      -- generic forests.
      WHEN leisure_val = 'nature_reserve'
        THEN leisure_val
      WHEN landuse_val IN (
        'park', 'forest', 'residential', 'retail', 'commercial', 'industrial',
	'railway', 'cemetery', 'grass', 'farmyard', 'farm', 'farmland', 'wood',
	'meadow', 'village_green', 'recreation_ground', 'allotments', 'quarry',
	'urban', 'rural', 'military')
        THEN landuse_val
      WHEN leisure_val IN (
        'park', 'garden', 'playground', 'golf_course', 'sports_centre', 'pitch',
	'stadium', 'common')
	THEN leisure_val
      WHEN natural_val IN (
        'wood', 'land', 'scrub', 'wetland', 'glacier', 'beach')
	THEN natural_val
      WHEN highway_val IN (
        'pedestrian', 'footway')
	THEN highway_val
      WHEN amenity_val IN (
        'university', 'school', 'college', 'library', 'fuel', 'parking',
	'cinema', 'theatre', 'place_of_worship', 'hospital')
	THEN amenity_val
      WHEN aeroway_val IN (
        'runway', 'taxiway', 'apron', 'aerodrome')
	THEN aeroway_val
      WHEN tourism_val IN (
        'zoo')
	THEN tourism_val
      WHEN man_made_val IN (
        'pier', 'wastewater_plant', 'works', 'bridge', 'tower', 'breakwater',
	'water_works', 'groyne', 'dike', 'cutline')
	THEN man_made_val
      WHEN power_val IN (
        'plant', 'generator', 'substation', 'station', 'sub_station')
	THEN power_val
      ELSE NULL END;
END;
$$ LANGUAGE plpgsql IMMUTABLE;

CREATE OR REPLACE FUNCTION mz_calculate_poi_level(
    aerialway_val text,
    aeroway_val text,
    amenity_val text,
    barrier_val text,
    craft_val text,
    highway_val text,
    historic_val text,
    leisure_val text,
    lock_val text,
    man_made_val text,
    natural_val text,
    office_val text,
    power_val text,
    railway_val text,
    shop_val text,
    tourism_val text,
    waterway_val text,
    way_area real
)
RETURNS REAL AS $$
DECLARE
  zoom REAL;
BEGIN
  zoom = mz_one_pixel_zoom(way_area);
  RETURN
    CASE
      WHEN aeroway_val IN ('aerodrome', 'airport')
        THEN LEAST(zoom + 4.12, 13)
      WHEN amenity_val = 'hospital'
        THEN LEAST(zoom + 3.32, 14)

      WHEN natural_val IN ('peak', 'volcano')
        THEN 11 -- these are generally point features
      WHEN railway_val IN ('station')
        THEN LEAST(zoom + 0.38, 13)
      WHEN tourism_val = 'zoo'
        THEN LEAST(zoom + 3.00, 15)
      WHEN (natural_val IN ('spring')
            OR railway_val IN ('level_crossing'))
        THEN 14 -- these are generally points
      WHEN amenity_val IN ('bank', 'cinema', 'courthouse', 'embassy',
          'fire_station', 'fuel', 'library', 'police', 'post_office',
	  'theatre')
        THEN LEAST(zoom + 2.7, 16)
      WHEN amenity_val IN ('biergarten', 'pub', 'bar', 'restaurant',
          'fast_food', 'cafe')
        THEN LEAST(zoom + 2.50, 17)
      WHEN (amenity_val IN ('pharmacy', 'veterinary')
            OR craft_val IN ('brewery', 'carpenter', 'confectionery', 'dressmaker',
                'electrician', 'gardener', 'handicraft', 'hvac', 'metal_construction',
                'painter', 'photographer', 'photographic_laboratory', 'plumber',
                'pottery', 'sawmill', 'shoemaker', 'stonemason', 'tailor', 'winery'))
        THEN LEAST(zoom + 3.3, 17)
      WHEN amenity_val  = 'nursing_home'     THEN LEAST(zoom + 1.25, 16)
      WHEN shop_val     = 'music'            THEN LEAST(zoom + 1.27, 17)
      WHEN amenity_val  = 'community_centre' THEN LEAST(zoom + 3.98, 17)
      WHEN shop_val     = 'sports'           THEN LEAST(zoom + 1.53, 17)
      WHEN amenity_val  = 'college'          THEN LEAST(zoom + 2.35, 16)
      WHEN shop_val     = 'mall'             THEN LEAST(zoom + 2.74, 17)
      WHEN leisure_val  = 'stadium'          THEN LEAST(zoom + 2.30, 15)
      WHEN amenity_val  = 'university'       THEN LEAST(zoom + 2.55, 15)
      WHEN tourism_val  = 'museum'           THEN LEAST(zoom + 1.43, 16)
      WHEN historic_val = 'landmark'         THEN LEAST(zoom + 1.76, 15)
      WHEN leisure_val  = 'marina'           THEN LEAST(zoom + 3.45, 17)
      WHEN amenity_val  = 'place_of_worship' THEN LEAST(2 * zoom - 9.55, 17)
      WHEN amenity_val  = 'townhall'         THEN LEAST(zoom + 1.85, 16)
      WHEN shop_val     = 'laundry'          THEN LEAST(zoom + 4.90, 17)
      WHEN shop_val     = 'dry_cleaning'     THEN LEAST(zoom + 4.90, 17)
      WHEN amenity_val  = 'ferry_terminal'   THEN LEAST(zoom + 3.20, 15)
      WHEN amenity_val  = 'school'           THEN LEAST(zoom + 2.30, 15)
      WHEN natural_val  = 'beach'            THEN LEAST(zoom + 3.20, 14)
      WHEN (barrier_val IN ('gate')
            OR craft_val IN ('sawmill')
            OR highway_val IN ('gate', 'mini_roundabout')
            OR lock_val IN ('yes')
            OR man_made_val IN ('lighthouse', 'power_wind')
            OR natural_val IN ('cave_entrance')
            OR power_val IN ('generator')
            OR waterway_val IN ('lock')
            OR aerialway_val IN ('station')
            OR railway_val IN ('halt', 'tram_stop')
            OR tourism_val IN ('alpine_hut'))
        THEN 15
      WHEN (aeroway_val IN ('helipad')
                   OR amenity_val IN ('bus_station', 'car_sharing',
                                      'picnic_site',
                                      'prison', 'recycling', 'shelter')
                   OR barrier_val IN ('block', 'bollard', 'lift_gate')
                   OR craft_val IN ('brewery', 'winery', 'sawmill')
                   OR highway_val IN ('ford')
                   OR historic_val IN ('archaeological_site')
                   OR man_made_val IN ('windmill')
                   OR natural_val IN ('tree')
                   OR shop_val IN ('department_store', 'supermarket')
                   OR tourism_val IN ('camp_site', 'caravan_site', 'information', 'viewpoint')) THEN 16
             WHEN (aeroway_val IN ('gate')
                   OR amenity_val IN (
                 'atm', 'bicycle_rental', 'bicycle_parking', 'bus_stop',
                 'drinking_water', 'emergency_phone',
                 'parking', 'post_box', 'telephone', 'theatre',
                 'toilets')
                   OR highway_val IN ('bus_stop', 'traffic_signals')
                   OR historic_val IN ('memorial')
                   OR leisure_val IN ('playground', 'slipway')
                   OR man_made_val IN ('mast', 'water_tower')
                   OR office_val IN ('accountant', 'administrative', 'advertising_agency',
                'architect', 'association', 'company', 'consulting', 'educational_institution',
                'employment_agency', 'estate_agent', 'financial', 'foundation', 'government',
                'insurance', 'it', 'lawyer', 'newspaper', 'ngo', 'notary', 'physician',
                'political_party', 'religion', 'research', 'tax_advisor', 'telecommunication',
                'therapist', 'travel_agent', 'yes')
                   OR shop_val IN ('bakery', 'bicycle', 'books', 'butcher', 'car', 'car_repair',
                                 'clothes', 'computer', 'convenience',
                                 'doityourself', 'dry_cleaning', 'fashion', 'florist', 'gift',
                                 'greengrocer', 'hairdresser', 'jewelry', 'mobile_phone',
                                 'optician', 'pet')
                   OR tourism_val IN ('bed_and_breakfast', 'chalet', 'guest_house',
                                    'hostel', 'hotel', 'motel')
                   OR railway_val IN ('subway_entrance')) THEN 17
             WHEN (amenity_val IN ('bench', 'waste_basket')) THEN 18
             ELSE NULL END;
END;
$$ LANGUAGE plpgsql IMMUTABLE;

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

CREATE OR REPLACE FUNCTION mz_calculate_railway_level(railway_val text, service_val text)
RETURNS SMALLINT AS $$
BEGIN
  RETURN CASE
    WHEN railway_val = 'rail' THEN CASE
      WHEN service_val IS NULL               THEN 11
      WHEN service_val IN ('spur', 'siding') THEN 12
      WHEN service_val IN ('yard')           THEN 13
      WHEN service_val IN ('crossover')      THEN 14
      ELSE                                        15
    END
    WHEN railway_val IN ('tram', 'light_rail', 'narrow_gauge', 'monorail') THEN 15
    ELSE NULL
  END;
END;
$$ LANGUAGE plpgsql IMMUTABLE;

CREATE OR REPLACE FUNCTION mz_calculate_highway_level(highway_val text, service_val text)
RETURNS SMALLINT AS $$
BEGIN
  RETURN CASE
    WHEN highway_val IN ('motorway', 'trunk', 'motorway_link', 'primary')     THEN  8
    WHEN highway_val IN ('secondary')                                         THEN 10
    WHEN highway_val IN ('tertiary')                                          THEN 11
    WHEN highway_val IN ('trunk_link', 'residential', 'unclassified', 'road') THEN 12
    WHEN highway_val IN ('primary_link', 'secondary_link', 'track',
                         'pedestrian', 'living_street')                       THEN 13
    WHEN highway_val IN ('tertiary_link', 'minor', 'footpath', 'footway',
                         'steps', 'path', 'cycleway')                         THEN 14
    WHEN highway_val = 'service' THEN CASE
      WHEN service_val IS NULL                                                THEN 14
      WHEN service_val = 'alley'                                              THEN 13
      WHEN service_val IN ('driveway', 'parking_aisle', 'drive-through')      THEN 15
      ELSE NULL
    END
    ELSE NULL
  END;
END;
$$ LANGUAGE plpgsql IMMUTABLE;

CREATE OR REPLACE FUNCTION mz_calculate_aeroway_level(aeroway_val text)
RETURNS SMALLINT AS $$
BEGIN
  RETURN CASE
    WHEN aeroway_val IN ('runway') THEN 9
    WHEN aeroway_val IN ('taxiway') THEN 11
    ELSE NULL
  END;
END;
$$ LANGUAGE plpgsql IMMUTABLE;

CREATE OR REPLACE FUNCTION mz_calculate_aerialway_level(aerialway_val text)
RETURNS SMALLINT AS $$
BEGIN
  RETURN CASE
    WHEN aerialway_val IN ('gondola', 'cable_car')                   THEN 12
    WHEN aerialway_val IN ('chair_lift')                             THEN 13
    WHEN aerialway_val IN ('drag_lift', 'platter', 't-bar', 'goods',
         'magic_carpet', 'rope_tow', 'yes', 'zip_line', 'j-bar',
         'unknown', 'mixed_lift', 'canopy', 'cableway')              THEN 15
    ELSE NULL
  END;
END;
$$ LANGUAGE plpgsql IMMUTABLE;

CREATE OR REPLACE FUNCTION mz_calculate_road_level(highway_val text, railway_val text, aeroway_val text, route_val text, service_val text, aerialway_val text, way geometry)
RETURNS SMALLINT AS $$
BEGIN
    RETURN LEAST(
      CASE WHEN highway_val IS NOT NULL
        THEN mz_calculate_highway_level(highway_val, service_val)
        ELSE NULL END,
      CASE WHEN aeroway_val IS NOT NULL
        THEN mz_calculate_aeroway_level(aeroway_val)
        ELSE NULL END,
      CASE WHEN railway_val IS NOT NULL
        THEN mz_calculate_railway_level(railway_val, service_val)
        ELSE NULL END,
      CASE WHEN route_val = 'ferry'
        THEN mz_calculate_ferry_level(way)
        ELSE NULL END,
      CASE WHEN aerialway_val IS NOT NULL
        THEN mz_calculate_aerialway_level(aerialway_val)
        ELSE NULL END);
END;
$$ LANGUAGE plpgsql IMMUTABLE;

CREATE OR REPLACE FUNCTION mz_calculate_is_water(
    waterway_val text, natural_val text, landuse_val text)
RETURNS BOOLEAN AS $$
BEGIN
    RETURN (
        waterway_val IN ('riverbank', 'dock')
     OR natural_val IN ('water')
     OR landuse_val IN ('basin', 'reservoir')
    );
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

CREATE OR REPLACE FUNCTION mz_calculate_transit_level(route_val text)
RETURNS SMALLINT AS $$
BEGIN
    RETURN (
        CASE WHEN route_val IN ('train', 'railway') THEN 6
             WHEN route_val IN ('subway', 'light_rail', 'tram') THEN 10
             ELSE NULL END
    );
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

-- mz_get_rel_network returns a network tag, or NULL, for a
-- given way ID.
--
-- it does this by joining onto the relations slim table, so it
-- won't work if you dropped the slim tables, or didn't use slim
-- mode in osm2pgsql.
--
CREATE OR REPLACE FUNCTION mz_get_rel_network(
  way_id bigint)
RETURNS text AS $$
BEGIN
  RETURN mz_first_dedup(ARRAY(
    SELECT mz_rel_get_tag(tags, 'network')
    FROM planet_osm_rels
    WHERE parts && ARRAY[way_id]
      AND parts[way_off+1:rel_off] && ARRAY[way_id]));
END;
$$ LANGUAGE plpgsql IMMUTABLE;

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

CREATE OR REPLACE FUNCTION mz_calculate_landuse_min_zoom(
  landuse_val TEXT,
  leisure_val TEXT,
  natural_val TEXT,
  highway_val TEXT,
  amenity_val TEXT,
  aeroway_val TEXT,
  tourism_val TEXT,
  man_made_val TEXT,
  power_val TEXT,
  boundary_val TEXT,
  way_area REAL)
RETURNS REAL AS $$
DECLARE
  zoom REAL;
BEGIN
  zoom = mz_one_pixel_zoom(way_area);
  RETURN
    CASE
      WHEN (boundary_val IN ('national_park', 'protected_area')
            OR leisure_val = 'nature_reserve')
        THEN zoom
      ELSE
        GREATEST(LEAST(zoom, 16), 9)
    END;
END;
$$ LANGUAGE plpgsql IMMUTABLE;


-- calculate the list of refs (or names) of transit routes that
-- a particular station is part of. this ends up being a very
-- complex function because it's bouncing around between the
-- nodes, ways and relations to calculate membership of various
-- sets.
CREATE OR REPLACE FUNCTION mz_calculate_transit_routes(
  station_node_id BIGINT)
RETURNS text[] AS $$
DECLARE
  -- IDs of "stop area" relations which contain the station nodes.
  -- each individual line may have its own stop node, and this is
  -- the relation which groups the stops together with the station.
  stop_area_ids      bigint[];

  -- IDs of nodes which are tagged as stations or stops and are
  -- members of the stop area relations. these will contain the
  -- original `station_node_id`, but probably many others as well.
  stations_and_stops bigint[];

  -- IDs of ways which contain any of the stations and stops.
  -- these are included because sometimes the stop node isn't
  -- directly included in the route relation, only the way
  -- representing the track itself.
  lines              bigint[];

BEGIN
  stop_area_ids := ARRAY(
    SELECT DISTINCT r.id
    FROM planet_osm_rels r
    WHERE r.parts && ARRAY[station_node_id]
    AND r.parts[1:r.way_off] && ARRAY[station_node_id]
    AND mz_rel_get_tag(r.tags, 'public_transport') = 'stop_area'
  );

  stations_and_stops := ARRAY(
    SELECT DISTINCT n.id
    FROM planet_osm_nodes n
    JOIN (SELECT DISTINCT unnest(r.parts[1:r.way_off]) AS node_id
          FROM planet_osm_rels r
	  WHERE r.id = ANY(stop_area_ids)) r
    ON r.node_id = n.id
    WHERE (
      mz_rel_get_tag(n.tags, 'railway') IN ('station', 'stop') OR
      mz_rel_get_tag(n.tags, 'public_transport') IN ('stop', 'stop_position'))
    -- manually re-include the original station node, in case it's
    -- not part of a public_transport=stop_area relation.
    UNION SELECT station_node_id AS id
  );

  lines := ARRAY(
    SELECT DISTINCT w.id
    FROM planet_osm_ways w
    WHERE w.nodes && stations_and_stops
    AND mz_rel_get_tag(w.tags, 'railway') IN ('subway', 'light_rail', 'tram', 'rail')
  );

  RETURN ARRAY(
    SELECT DISTINCT trim(both from "name")
    FROM (
      SELECT unnest(string_to_array(COALESCE(
          -- prefer ref as it's less likely to contain the destination name
          mz_rel_get_tag(tags, 'ref'),
          mz_rel_get_tag(tags, 'name')
        ), ',')) AS "name"
      FROM planet_osm_rels
      WHERE ((
          parts && stations_and_stops AND
          parts[1:way_off] && stations_and_stops
        ) OR (
          parts && lines AND
          parts[way_off+1:rel_off] && lines
        )) AND
        mz_rel_get_tag(tags, 'type') = 'route' AND
        mz_rel_get_tag(tags, 'route') IN ('subway', 'light_rail', 'tram', 'train')
      ) subquery
    );
END;
$$ LANGUAGE plpgsql IMMUTABLE;

-- returns true if the text is numeric and can be cast
-- to a float without error.
CREATE OR REPLACE FUNCTION mz_is_numeric(
  t text)
RETURNS BOOLEAN AS $$
BEGIN
  RETURN t ~ '^([0-9]+[.]?[0-9]*|[.][0-9]+)$';
END;
$$ LANGUAGE plpgsql IMMUTABLE;

-- replicate some of the backend logic for filtering
-- buildings, as there are lots and lots and lots of
-- these, often with quite complex geometries, and
-- we don't want to saturate the network with lots of
-- buildings at z13 that we're going to filter out.
CREATE OR REPLACE FUNCTION mz_building_filter(
  height text, levels text, way_area FLOAT, min_volume FLOAT, min_area FLOAT)
RETURNS BOOLEAN AS $$
BEGIN
  RETURN CASE
    -- if height is present, and can be parsed as a
    -- float, then we can filter right here.
    WHEN mz_is_numeric(height)
      THEN (height::float * way_area) >= min_volume

    -- looks like we assume each level is 3m, plus
    -- 2 overall.
    WHEN mz_is_numeric(levels)
      THEN ((GREATEST(levels::float, 1) * 3 + 2) * way_area) >= min_volume

    -- if height is present, but not numeric, then
    -- we have no idea what it could be, and we must
    -- assume it could be very large.
    WHEN height IS NOT NULL OR levels IS NOT NULL
      THEN TRUE

    -- height isn't present, so just filter on area
    -- as we did before.
    ELSE way_area >= min_area
  END;
END;
$$ LANGUAGE plpgsql IMMUTABLE;
