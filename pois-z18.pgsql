SELECT name,
       COALESCE("aerialway", "aeroway", "amenity", "barrier", "highway", "historic",
                "leisure", "lock", "man_made", "natural", "power", "railway", "shop",
                "tourism", "waterway") AS kind,
       way AS __geometry__,
       osm_id AS __id__

FROM planet_osm_point

WHERE (
      "aerialway" IN ('station')
   OR "aeroway" IN ('aerodrome', 'airport', 'helipad')
   OR "amenity" IN ('atm', 'bank', 'bar', 'bench', 'bicycle_rental', 'biergarten',
                    'bus_station', 'bus_stop', 'cafe', 'car_sharing', 'cinema',
                    'courthouse', 'drinking_water', 'embassy', 'emergency_phone',
                    'fast_food', 'fire_station', 'fuel', 'hospital', 'library',
                    'parking', 'pharmacy', 'picnic_site', 'place_of_worship',
                    'police', 'post_box', 'post_office', 'prison', 'pub',
                    'recycling', 'restaurant', 'shelter', 'telephone', 'theatre',
                    'toilets', 'veterinary', 'waste_basket')
   OR "barrier" IN ('block', 'bollard', 'gate', 'lift_gate')
   OR "highway" IN ('bus_stop', 'ford', 'gate', 'mini_roundabout', 'traffic_signals')
   OR "historic" IN ('archaeological_site', 'memorial')
   OR "leisure" IN ('playground', 'slipway')
   OR "lock" IN ('yes')
   OR "man_made" IN ('lighthouse', 'mast', 'power_wind', 'water_tower', 'windmill')
   OR "natural" IN ('cave_entrance', 'peak', 'spring', 'tree', 'volcano')
   OR "power" IN ('generator')
   OR "railway" IN ('halt', 'level_crossing', 'station', 'subway_entrance', 'tram_stop')
   OR "shop" IN ('bakery', 'bicycle', 'books', 'butcher', 'car', 'car_repair',
                 'clothes', 'computer', 'convenience', 'department_store',
                 'doityourself', 'dry_cleaning', 'fashion', 'florist', 'gift',
                 'greengrocer', 'hairdresser', 'jewelry', 'mobile_phone',
                 'optician', 'pet', 'supermarket')
   OR "tourism" IN ('alpine_hut', 'bed_and_breakfast', 'camp_site', 'caravan_site',
                    'chalet', 'guest_house', 'hostel', 'hotel', 'information',
                    'motel', 'museum', 'viewpoint')
   OR "waterway" IN ('lock')
)
