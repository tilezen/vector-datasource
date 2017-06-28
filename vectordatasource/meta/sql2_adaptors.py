layer_tables = {
    'boundaries': [
        'ne_10m_admin_0_boundary_lines_land',
        'ne_10m_admin_0_boundary_lines_map_units',
        'ne_10m_admin_1_states_provinces_lines',
        'ne_110m_admin_0_boundary_lines_land',
        'ne_50m_admin_0_boundary_lines_land',
        'ne_50m_admin_1_states_provinces_lines',
        'planet_osm_line',
        'planet_osm_polygon',
    ],
    'buildings': [
        'planet_osm_point',
        'planet_osm_polygon',
    ],
    'earth': [
        'land_polygons',
        'ne_10m_land',
        'ne_110m_land',
        'ne_50m_land',
        'planet_osm_line',
        'planet_osm_point',
        'planet_osm_polygon',
    ],
    'landuse': [
        'planet_osm_line',
        'planet_osm_polygon',
    ],
    'places': [
        'ne_10m_populated_places',
        'planet_osm_point',
    ],
    'pois': [
        'planet_osm_point',
        'planet_osm_polygon',
    ],
    'roads': [
        'ne_10m_roads',
        'planet_osm_line',
    ],
    'transit': [
        'planet_osm_line',
        'planet_osm_polygon',
    ],
    'water': [
        'ne_10m_coastline',
        'ne_10m_lakes',
        'ne_10m_ocean',
        'ne_10m_playas',
        'ne_110m_coastline',
        'ne_110m_lakes',
        'ne_110m_ocean',
        'ne_50m_coastline',
        'ne_50m_lakes',
        'ne_50m_ocean',
        'ne_50m_playas',
        'planet_osm_line',
        'planet_osm_point',
        'planet_osm_polygon',
        'water_polygons',
    ],
}


POLYGON_TABLES = [
    'planet_osm_polygon',
    'buffered_land',
    'land_polygons',
    'ne_10m_lakes',
    'ne_10m_land',
    'ne_10m_ocean',
    'ne_10m_playas',
    'ne_10m_urban_areas',
    'ne_110m_lakes',
    'ne_110m_land',
    'ne_110m_ocean',
    'ne_50m_lakes',
    'ne_50m_land',
    'ne_50m_ocean',
    'ne_50m_playas',
    'ne_50m_urban_areas',
    'water_polygons',
]


def table_is_osm(name):
    return name.startswith('planet_osm_')


def table_is_polygonal(name):
    return name in POLYGON_TABLES


HEADER = """CREATE OR REPLACE FUNCTION mz2_calculate_%(calc)s_%(layer)s(%(table)s)
RETURNS %(return_type)s AS $$
DECLARE
  row ALIAS FOR $1;
BEGIN"""


FOOTER = """END;
$$ LANGUAGE plpgsql IMMUTABLE;
"""


OSM_TABLE = """RETURN mz2_calculate_%(calc)s_%(layer)s_(row.osm_id, row.way, row.tags, %(way_area)s);"""


NON_OSM_TABLE = "RETURN mz2_calculate_%(calc)s_%(layer)s_(row.gid, row.%(geom_column)s, hstore(row), %(way_area)s);"


for layer, tables in layer_tables.items():
    for table in tables:
        for calc, return_type in [('json', 'JSON'), ('min_zoom', 'REAL')]:
            if table_is_polygonal(table):
                way_area = 'row.way_area'
            else:
                way_area = '0::real'

            var = dict(layer=layer, table=table, geom_column='the_geom',
                       calc=calc, return_type=return_type, way_area=way_area)

            print HEADER % var

            if table_is_osm(table):
                print OSM_TABLE % var

            else:
                print NON_OSM_TABLE % var

            print FOOTER
