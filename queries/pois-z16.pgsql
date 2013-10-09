SELECT name,
       COALESCE("aerialway", "aeroway", "amenity", "barrier", "highway", "historic",
                "lock", "man_made", "natural", "power", "railway", "shop", "tourism",
                "waterway") AS kind,
       way AS __geometry__,
       osm_id AS __id__

FROM planet_osm_point

WHERE (
      "aerialway" IN ('station')
   OR "aeroway" IN ('aerodrome', 'airport', 'helipad')
   OR "amenity" IN ('biergarten', 'bus_station', 'bus_stop', 'car_sharing',
                    'hospital', 'parking', 'picnic_site', 'place_of_worship',
                    'prison', 'pub', 'recycling', 'shelter')
   OR "barrier" IN ('block', 'bollard', 'gate', 'lift_gate')
   OR "highway" IN ('bus_stop', 'ford', 'gate', 'mini_roundabout')
   OR "historic" IN ('archaeological_site')
   OR "lock" IN ('yes')
   OR "man_made" IN ('lighthouse', 'power_wind', 'windmill')
   OR "natural" IN ('cave_entrance', 'peak', 'spring', 'tree', 'volcano')
   OR "power" IN ('generator')
   OR "railway" IN ('halt', 'level_crossing', 'station', 'tram_stop')
   OR "shop" IN ('department_store', 'supermarket')
   OR "tourism" IN ('alpine_hut', 'camp_site', 'caravan_site', 'information', 'viewpoint')
   OR "waterway" IN ('lock')
)
