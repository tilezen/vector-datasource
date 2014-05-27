SELECT name,
       COALESCE("aeroway") AS kind,
       way AS __geometry__,
       osm_id AS __id__,
       "aeroway"

FROM planet_osm_point

WHERE (
      "aeroway" IN ('aerodrome', 'airport')
)
