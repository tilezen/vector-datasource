SELECT
    way AS __geometry__,
    name,
    osm_id,
    osm_id::text AS __id__,
    aeroway,
    bridge,
    highway,
    layer,
    railway,
    tunnel

FROM planet_osm_line

WHERE
    mz_calculate_road_level(highway, railway, aeroway) <= 10
