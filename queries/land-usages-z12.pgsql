SELECT name,
       ST_Area(way)::bigint AS area,
       COALESCE("landuse", "leisure", "natural", "highway", "amenity") AS kind,
       'openstreetmap.org' AS source,
       way AS __geometry__,
    
       --
       -- Negative osm_id is synthetic, with possibly multiple geometry rows.
       --
       (CASE WHEN osm_id < 0 THEN Substr(MD5(ST_AsBinary(way)), 1, 10)
             ELSE osm_id::varchar END) AS __id__

FROM planet_osm_polygon

WHERE (
      "landuse" IN ('park', 'forest', 'residential', 'retail', 'commercial',
                    'industrial', 'railway', 'cemetery', 'grass', 'farmyard',
                    'farm', 'farmland', 'wood', 'meadow', 'village_green',
                    'recreation_ground', 'allotments', 'quarry')
   OR "leisure" IN ('park', 'garden', 'playground', 'golf_course', 'sports_centre',
                    'pitch', 'stadium', 'common', 'nature_reserve')
   OR "natural" IN ('wood', 'land', 'scrub')
   OR "highway" IN ('pedestrian', 'footway')
   OR "amenity" IN ('university', 'school', 'college', 'library', 'fuel',
                    'parking', 'cinema', 'theatre', 'place_of_worship', 'hospital')
   )
   AND ST_Area(way) > 6400 -- 4px
