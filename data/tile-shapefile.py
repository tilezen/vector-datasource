import sys

import fiona
import shapely.geometry

shapefile_source = sys.argv[1]
shapefile_sink = sys.argv[2]

# meters in a z5 tile
chunk_dim_meters = 1252344


def tile(geometry, chunk_dim_meters=chunk_dim_meters):
    # NOTE: these are not aligned to tile coordinates
    minx, miny, maxx, maxy = geometry.bounds
    tiled_polys = []
    y = miny
    while y < maxy:
        x = minx
        endy = y + chunk_dim_meters
        while x < maxx:
            endx = x + chunk_dim_meters
            tile_bounds = shapely.geometry.box(x, y, endx, endy)
            tiled_poly = geometry.intersection(tile_bounds)
            if not tiled_poly.is_empty:
                tiled_polys.append(tiled_poly)

            x += chunk_dim_meters

        y += chunk_dim_meters

    return tiled_polys


with fiona.Env():

    with fiona.open(shapefile_source) as source:

        meta = source.meta

        tiled_features = []
        for f in source:
            geometry = f['geometry']
            shape = shapely.geometry.shape(geometry)
            assert shape.type in ('MultiPolygon', 'Polygon'), \
                'Expecting polygons, not %s' % shape.type

            tiled_polys = []
            if shape.type == 'MultiPolygon':
                for poly in shape.geoms:
                    tiled_polys.extend(tile(poly))
            else:
                tiled_polys.extend(tile(shape))

            for i, tile_poly in enumerate(tiled_polys):
                tiled_feature = f.copy()
                tiled_feature['id'] = i + 1
                tiled_feature['geometry'] = tile_poly.__geo_interface__
                tiled_features.append(tiled_feature)

        with fiona.open(shapefile_sink, 'w', **meta) as sink:
            for f in tiled_features:
                sink.write(f)
