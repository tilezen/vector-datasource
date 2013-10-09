SELECT name,
       COALESCE("aeroway", "natural", "railway") AS kind,
       way AS __geometry__,
       osm_id AS __id__

FROM planet_osm_point

WHERE (
      "aeroway" IN ('aerodrome', 'airport')
   OR "natural" IN ('peak', 'volcano')
   OR "railway" IN ('station')
)
