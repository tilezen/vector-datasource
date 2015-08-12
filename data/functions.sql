CREATE OR REPLACE FUNCTION mz_calculate_is_landuse(
    landuse_val text, leisure_val text, natural_val text, highway_val text, amenity_val text, aeroway_val text)
RETURNS BOOLEAN AS $$
BEGIN
    RETURN
        landuse_val IN ('park', 'forest', 'residential', 'retail', 'commercial',
                        'industrial', 'railway', 'cemetery', 'grass', 'farmyard',
                        'farm', 'farmland', 'wood', 'meadow', 'village_green',
                        'recreation_ground', 'allotments', 'quarry')
     OR leisure_val IN ('park', 'garden', 'playground', 'golf_course', 'sports_centre',
                        'pitch', 'stadium', 'common', 'nature_reserve')
     OR natural_val IN ('wood', 'land', 'scrub', 'wetland', 'glacier')
     OR highway_val IN ('pedestrian', 'footway')
     OR amenity_val IN ('university', 'school', 'college', 'library', 'fuel',
                        'parking', 'cinema', 'theatre', 'place_of_worship', 'hospital')
     OR aeroway_val IN ('runway', 'taxiway', 'apron');
END;
$$ LANGUAGE plpgsql IMMUTABLE;

CREATE OR REPLACE FUNCTION mz_calculate_poi_level(
    aerialway_val text,
    aeroway_val text,
    amenity_val text,
    barrier_val text,
    highway_val text,
    historic_val text,
    leisure_val text,
    lock_val text,
    man_made_val text,
    natural_val text,
    power_val text,
    railway_val text,
    shop_val text,
    tourism_val text,
    waterway_val text
)
RETURNS SMALLINT AS $$
BEGIN
    RETURN (
        CASE WHEN aeroway_val IN ('aerodrome', 'airport') THEN 9
             WHEN natural_val IN ('peak', 'volcano') THEN 11
             WHEN railway_val IN ('station') THEN 12
             WHEN (aerialway_val IN ('station')
                   OR railway_val IN ('halt', 'tram_stop')
                   OR tourism_val IN ('alpine_hut')) THEN 13
             WHEN (natural_val IN ('spring')
                   OR railway_val IN ('level_crossing')) THEN 14
             WHEN (amenity_val IN ('hospital')
                   OR barrier_val IN ('gate')
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
                   OR highway_val IN ('bus_stop', 'traffic_signals')
                   OR historic_val IN ('memorial')
                   OR leisure_val IN ('playground', 'slipway')
                   OR man_made_val IN ('mast', 'water_tower')
                   OR shop_val IN ('bakery', 'bicycle', 'books', 'butcher', 'car', 'car_repair',
                                 'clothes', 'computer', 'convenience',
                                 'doityourself', 'dry_cleaning', 'fashion', 'florist', 'gift',
                                 'greengrocer', 'hairdresser', 'jewelry', 'mobile_phone',
                                 'optician', 'pet')
                   OR tourism_val IN ('bed_and_breakfast', 'chalet', 'guest_house',
                                    'hostel', 'hotel', 'motel', 'museum')
                   OR railway_val IN ('subway_entrance')) THEN 17
             WHEN (amenity_val IN ('bench', 'waste_basket')) THEN 18
             ELSE NULL END
    );
END;
$$ LANGUAGE plpgsql IMMUTABLE;

CREATE OR REPLACE FUNCTION mz_calculate_road_level(highway_val text, railway_val text, aeroway_val text, network_val text)
RETURNS SMALLINT AS $$
BEGIN
    RETURN (
        CASE WHEN (highway_val IN ('motorway', 'trunk', 'primary', 'motorway_link') OR network_val='US:I') THEN 9
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
