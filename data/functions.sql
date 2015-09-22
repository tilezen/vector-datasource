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
     OR natural_val IN ('wood', 'land', 'scrub', 'wetland', 'glacier')
     OR highway_val IN ('pedestrian', 'footway')
     OR amenity_val IN ('university', 'school', 'college', 'library', 'fuel',
                        'parking', 'cinema', 'theatre', 'place_of_worship', 'hospital')
     OR aeroway_val IN ('runway', 'taxiway', 'apron', 'aerodrome')
     OR tourism_val IN ('zoo')
     OR man_made_val IN ('pier', 'wastewater_plant', 'works', 'bridge', 'tower',
                         'breakwater', 'water_works', 'groyne', 'dike', 'cutline')
     OR power_val IN   ('plant', 'generator', 'substation', 'station', 'sub_station')
     OR boundary_val IN ('national_park');
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
RETURNS SMALLINT AS $$
DECLARE
  zoom smallint;
BEGIN
  zoom =
        CASE WHEN natural_val IN ('peak', 'volcano') THEN 11
             WHEN railway_val IN ('station') THEN 12
             WHEN (aeroway_val IN ('aerodrome', 'airport')
                   OR aerialway_val IN ('station')
                   OR railway_val IN ('halt', 'tram_stop')
                   OR tourism_val IN ('alpine_hut', 'zoo')) THEN 13
             WHEN (natural_val IN ('spring')
                   OR railway_val IN ('level_crossing')) THEN 14
             WHEN (amenity_val IN ('hospital')
                   OR barrier_val IN ('gate')
                   OR craft_val IN ('sawmill')
                   OR highway_val IN ('gate', 'mini_roundabout')
                   OR lock_val IN ('yes')
                   OR man_made_val IN ('lighthouse', 'power_wind')
                   OR natural_val IN ('cave_entrance')
                   OR power_val IN ('generator')
                   OR waterway_val IN ('lock')) THEN 15
             WHEN (aeroway_val IN ('helipad')
                   OR amenity_val IN ('biergarten', 'bus_station', 'car_sharing',
                                      'picnic_site', 'place_of_worship',
                                      'prison', 'pub', 'recycling', 'shelter')
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
                 'atm', 'bank', 'bar', 'bicycle_rental', 'bicycle_parking', 'bus_stop',
                 'cafe', 'cinema', 'courthouse', 'drinking_water', 'embassy', 'emergency_phone',
                 'fast_food', 'fire_station', 'fuel', 'library', 'parking', 'pharmacy',
                 'police', 'post_box', 'post_office', 'restaurant', 'telephone', 'theatre',
                 'toilets', 'veterinary')
                   OR craft_val IN ('brewery', 'carpenter', 'confectionery', 'dressmaker',
                'electrician', 'gardener', 'handicraft', 'hvac', 'metal_construction',
                'painter', 'photographer', 'photographic_laboratory', 'plumber',
                'pottery', 'sawmill', 'shoemaker', 'stonemason', 'tailor', 'winery')
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
                                    'hostel', 'hotel', 'motel', 'museum')
                   OR railway_val IN ('subway_entrance')) THEN 17
             WHEN (amenity_val IN ('bench', 'waste_basket')) THEN 18
             ELSE NULL END;
  RETURN (CASE
    WHEN way_area > 1.0e7 THEN zoom - 4
    WHEN way_area > 1.0e6 THEN zoom - 3
    WHEN way_area > 1.0e5 THEN zoom - 2
    WHEN way_area > 1.0e4 THEN zoom - 1
    ELSE zoom END);
END;
$$ LANGUAGE plpgsql IMMUTABLE;

CREATE OR REPLACE FUNCTION mz_calculate_road_level(highway_val text, railway_val text, aeroway_val text)
RETURNS SMALLINT AS $$
BEGIN
    RETURN (
        CASE WHEN highway_val IN ('motorway', 'trunk', 'primary', 'motorway_link') THEN 9
             WHEN highway_val IN ('secondary') THEN 10
             WHEN (highway_val IN ('tertiary')
                OR aeroway_val IN ('runway', 'taxiway')) THEN 11
             WHEN highway_val IN ('trunk_link', 'residential', 'unclassified', 'road') THEN 12
             WHEN highway_val IN ('primary_link', 'secondary_link') THEN 13
             WHEN (highway_val IN ('tertiary_link', 'minor')
                OR railway_val='rail') THEN 14
             WHEN (highway_val IN ('service', 'footpath', 'track', 'footway', 'steps', 'pedestrian', 'path', 'cycleway', 'living_street')
                OR railway_val IN ('tram', 'light_rail', 'narrow_gauge', 'monorail')) THEN 15
             ELSE NULL END
    );
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
    RETURN (building_val IS NOT NULL OR buildingpart_val IS NOT NULL);
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
  RETURN (17.256-ln(way_area)/ln(4));
END;
$$ LANGUAGE plpgsql IMMUTABLE;
