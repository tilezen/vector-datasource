from vectordatasource.transform import _Params
from vectordatasource.transform import _find_layer
from tilequeue.tile import mercator_point_to_coord
from tilequeue.tile import coord_to_mercator_point
from tilequeue.tile import calc_meters_per_pixel_dim
from ModestMaps.Core import Coordinate
from os.path import join as path_join
from collections import defaultdict


class _UrlPattern(object):
    def __init__(self, pattern):
        self.pattern = pattern

    def __call__(self, coord):
        return self.pattern.\
            replace("{z}", str(coord.zoom)).\
            replace("{x}", str(coord.column)).\
            replace("{y}", str(coord.row))


def _geotransform(topleft, bottomright, width, height):
    ul_x, ul_y = coord_to_mercator_point(topleft)
    lr_x, lr_y = coord_to_mercator_point(bottomright.down().right())
    minx = min(ul_x, lr_x)
    miny = min(ul_y, lr_y)
    maxx = max(ul_x, lr_x)
    maxy = max(ul_y, lr_y)
    return (minx, (maxx - minx) / width, 0,
            maxy, 0, (miny - maxy) / height)


def _memoize(f):
    result = {}

    def wrapped(*args, **kwargs):
        cache_key = tuple(args)
        if cache_key not in result:
            result[cache_key] = f(*args, **kwargs)
        return result[cache_key]

    return wrapped


def _polar(xy):
    from math import atan2
    x, y = xy
    return (x**2 + y**2, atan2(y, x))


@_memoize
def _neighbourhood(radius):
    """
    Return a list of (dx, dy) offsets which make up a spiral search of the
    given radius around a point.
    """

    r_squared = radius**2

    pts = []
    for x in xrange(-radius, radius + 1):
        for y in xrange(-radius, radius + 1):
            # we want to keep only points within the given distance of the
            # central point.
            if x**2 + y**2 <= r_squared:
                pts.append((x, y))

    # sort the points so that we examine nearby ones first.
    pts = sorted(pts, key=_polar)

    # discard first point, which will be the offset (0, 0), which is the
    # original point and therefore not in the neighbourhood of the original
    # point.
    return pts[1:]


def _get_tile(session, url_pattern, zoom, x, y, retries=3):
    from time import sleep
    from sys import stderr

    coord = Coordinate(zoom=zoom, column=x, row=y)
    url = url_pattern(coord)

    count = 0
    while count < retries:
        print>>stderr, "GET: %r" % (url,)
        response = session.get(url)
        if response.status_code == 200:
            return response
        print>>stderr, "FAILED [%d/%d], backing off for %d" % (count, retries, 2**count)
        sleep(2 ** count)
        count += 1

    raise Exception("Failed to fetch tile %r: status = %r after %d retries" %
                    (url, response.status_code, count))


def _download_raster_png(bounds, zoom, url_pattern, mem_drv, srs,
                         median_filter_size=3, cache=None, retries=3):
    """
    Download the tiles covering bounds at zoom level using the given URL
    pattern and store them in a new raster created from mem_drv with the
    coordinate system srs.
    """

    import requests
    from cachecontrol import CacheControl
    from cachecontrol.caches.file_cache import FileCache
    from PIL import Image
    from cStringIO import StringIO
    from tilequeue.tile import half_earth_circum
    from osgeo import gdal

    url = _UrlPattern(url_pattern)
    tile_size = 256
    water_search_radius = 2 * median_filter_size

    session = requests.Session()
    if cache:
        session = CacheControl(session, cache=FileCache(cache))

    def _clip(x):
        if x < -half_earth_circum:
            return -half_earth_circum
        if x > half_earth_circum:
            return half_earth_circum
        return x

    meters_per_px = calc_meters_per_pixel_dim(zoom)
    margin = meters_per_px * median_filter_size
    topleft = mercator_point_to_coord(
        zoom, _clip(bounds[0] - margin), _clip(bounds[3] + margin))
    bottomright = mercator_point_to_coord(
        zoom, _clip(bounds[2] + margin), _clip(bounds[1] - margin))

    minx = int(topleft.column)
    miny = int(topleft.row)
    maxx = int(bottomright.column)
    maxy = int(bottomright.row)

    coord_end = 1 << zoom
    assert 0 <= minx < coord_end
    assert 0 <= miny < coord_end
    assert 0 <= maxx < coord_end
    assert 0 <= maxy < coord_end

    width = tile_size * (maxx - minx + 1)
    height = tile_size * (maxy - miny + 1)

    im = Image.new('RGBA', (width, height))

    for x in xrange(minx, maxx + 1):
        for y in xrange(miny, maxy + 1):
            response = _get_tile(session, url, zoom, x, y, retries=retries)

            io = StringIO(response.content)
            tile = Image.open(io)

            assert tile.mode == 'P'
            assert tile.size == (tile_size, tile_size)
            dx = x - minx
            dy = y - miny
            im.paste(tile, (dx * tile_size, dy * tile_size))

    # drop down to just the red channel!
    im = im.getchannel("R")

    # TODO: configurable
    water = 69

    im2 = Image.new('L', (width, height))
    for x in xrange(median_filter_size, width - median_filter_size):
        for y in xrange(median_filter_size, height - median_filter_size):
            mid = im.getpixel((x, y))

            if mid == water:
                # for water, find the nearest non-water colour and use that
                for dx, dy in _neighbourhood(water_search_radius):
                    if 0 <= (x + dx) < width and 0 <= (y + dy) < height:
                        pt = im.getpixel((x + dx, y + dy))
                        if pt != water:
                            mid = pt
                            break

            else:
                # for non-water, do a modal filter (most common colour in
                # neighbourhood which isn't water)
                counts = defaultdict(lambda: 0)
                counts[mid] += 1
                for dx, dy in _neighbourhood(median_filter_size):
                    pt = im.getpixel((x + dx, y + dy))
                    if pt != water:
                        counts[pt] += 1
                max_count = 0
                max_colour = None
                for colour, count in counts.iteritems():
                    if count > max_count or \
                       (count == max_count and colour > max_colour):
                        max_count = count
                        max_colour = colour
                assert max_colour is not None
                mid = max_colour

            im2.putpixel((x, y), mid)

    ds = mem_drv.Create('', width, height, 1, gdal.GDT_Byte)
    ds.SetProjection(srs.ExportToWkt())
    ds.SetGeoTransform(_geotransform(topleft, bottomright, width, height))

    band = ds.GetRasterBand(1)
    band.WriteRaster(
        0, 0, width, height, im2.tobytes(),
        buf_xsize=width, buf_ysize=height,
        buf_type=gdal.GDT_Byte)

    return ds


def inject(ctx):
    """
    Inject some landcover polygons.
    """
    from osgeo import gdal
    from osgeo import osr
    from osgeo import ogr
    from shapely.wkb import loads as wkb_loads

    params = _Params(ctx, 'landcover.inject')
    layer_name = params.required('layer')
    url_pattern = params.required('url')
    kinds_mapping = params.required('kinds', typ=dict)
    cache = params.optional('cache')
    median_filter_size = params.optional('median-size', default=3, typ=int)
    clipping_layer_name = params.optional('clipping-layer', default='water')
    area_in_pixels = params.optional('area-in-pixels', typ=int)
    retries = params.optional('retries', typ=int, default=3)

    # sensible default?
    if area_in_pixels is None:
        area_in_pixels = 4 * median_filter_size ** 2

    layer = _find_layer(ctx.feature_layers, layer_name)
    features = layer['features']

    clipping_layer = _find_layer(ctx.feature_layers, clipping_layer_name)
    clipping_shapes = []
    for shape, props, fid in clipping_layer['features']:
        if shape.geom_type in ('Polygon', 'MultiPolygon'):
            clipping_shapes.append(shape)

    srs = osr.SpatialReference()
    srs.ImportFromEPSG(3857)
    mem_drv = gdal.GetDriverByName('MEM')

    ds = _download_raster_png(
        ctx.unpadded_bounds, ctx.nominal_zoom, url_pattern,
        mem_drv, srs, median_filter_size, cache, retries)
    assert ds is not None
    band = ds.GetRasterBand(1)

    sieve_ds = mem_drv.Create('', band.XSize, band.YSize, 1, gdal.GDT_Byte)
    sieve_ds.SetProjection(srs.ExportToWkt())
    sieve_ds.SetGeoTransform(ds.GetGeoTransform())
    dst_band = sieve_ds.GetRasterBand(1)
    gdal.SieveFilter(band, None, dst_band, area_in_pixels, 4)

    ogr_layername = 'layer'
    drv = ogr.GetDriverByName('memory')
    dst_ds = drv.CreateDataSource('')
    ogr_layer = dst_ds.CreateLayer(
        ogr_layername, geom_type=ogr.wkbPolygon, srs=srs)
    field = ogr.FieldDefn('Red', ogr.OFTInteger)
    ogr_layer.CreateField(field)

    gdal.Polygonize(dst_band, None, ogr_layer, 0, [], None)

    for feature in ogr_layer:
        red = feature.GetField('Red')
        kind_detail = kinds_mapping.get(red)

        if kind_detail:
            ogr_geom = feature.GetGeometryRef()
            shape = wkb_loads(ogr_geom.ExportToWkb())

            props = {'kind': 'landcover', 'kind_detail': kind_detail}
            for clipping_shape in clipping_shapes:
                shape = shape.difference(clipping_shape)

            if not shape.is_empty:
                # try the old "make valid" trick, as some of the polygons
                # coming from GDAL aren't valid (?!)
                if not shape.is_valid:
                    shape = shape.buffer(0)

                if shape.is_valid:
                    features.append((shape, props, None))

    # otherwise GDAL won't free any resources!
    del ds
    del dst_ds
    del sieve_ds
    del mem_drv

    return layer
