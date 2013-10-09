SELECT name,
       COALESCE("aerialway", "aeroway", "amenity", "barrier", "highway",
                "lock", "man_made", "natural", "power", "railway", "tourism",
                "waterway") AS kind,
       way AS __geometry__,
       osm_id AS __id__

FROM planet_osm_point

WHERE (
      "aerialway" IN ('station')
   OR "aeroway" IN ('aerodrome', 'airport')
   OR "amenity" IN ('hospital', 'parking')
   OR "barrier" IN ('gate')
   OR "highway" IN ('gate', 'mini_roundabout')
   OR "lock" IN ('yes')
   OR "man_made" IN ('lighthouse', 'power_wind')
   OR "natural" IN ('cave_entrance', 'peak', 'spring', 'volcano')
   OR "power" IN ('generator')
   OR "railway" IN ('halt', 'level_crossing', 'station', 'tram_stop')
   OR "tourism" IN ('alpine_hut')
   OR "waterway" IN ('lock')
)
