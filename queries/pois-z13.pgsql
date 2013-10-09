SELECT name,
       COALESCE("aerialway", "aeroway", "natural", "railway", "tourism") AS kind,
       way AS __geometry__,
       osm_id AS __id__

FROM planet_osm_point

WHERE (
      "aerialway" IN ('station')
   OR "aeroway" IN ('aerodrome', 'airport')
   OR "natural" IN ('peak', 'volcano')
   OR "railway" IN ('halt', 'station', 'tram_stop')
   OR "tourism" IN ('alpine_hut')
)
