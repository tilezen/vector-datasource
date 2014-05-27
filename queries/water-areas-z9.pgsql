SELECT name, area, kind, source, __geometry__, __id__

FROM
(
    --
    -- Ocean
    --
    SELECT '' AS name,
           ST_Area(the_geom)::bigint AS area,
           'ocean' AS kind,
           'openstreetmapdata.com' AS source,
           the_geom AS __geometry__,
           gid::varchar AS __id__
    
    FROM water_polygons
    
    WHERE the_geom && !bbox!
    
    --
    -- Other water areas
    --
    UNION

    SELECT name,
           ST_Area(way)::bigint AS area,
           COALESCE("waterway", "natural", "landuse") AS kind,
           'openstreetmap.org' AS source,
           way AS __geometry__,
        
           --
           -- Negative osm_id is synthetic, with possibly multiple geometry rows.
           --
           (CASE WHEN osm_id < 0 THEN Substr(MD5(ST_AsBinary(way)), 1, 10)
                 ELSE osm_id::varchar END) AS __id__
    
    FROM planet_osm_polygon
    
    WHERE (
         "waterway" IN ('riverbank')
       OR "natural" IN ('water')
       OR "landuse" IN ('basin', 'reservoir')
       )
       AND ST_Area(way) > 102400 -- 4px
       AND way && !bbox!

) AS water_areas
