SELECT name,
       COALESCE("aeroway", "natural") AS kind,
       way AS __geometry__,
       osm_id AS __id__,
       "aeroway", "natural"

FROM planet_osm_point

WHERE (
      "aeroway" IN ('aerodrome', 'airport')
   OR "natural" IN ('peak', 'volcano')
)
