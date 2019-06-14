from vectordatasource.transform import _Params
from vectordatasource.transform import _find_layer
from tilequeue.tile import mercator_point_to_coord
from tilequeue.tile import coord_to_mercator_point
from ModestMaps.Core import Coordinate
from os.path import join as path_join


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


def _download_raster_png(bounds, zoom, url_pattern, output_file,
                         median_filter_size=3, cache=None):
    """
    Download the tiles covering bounds at zoom level using the given URL
    pattern and store them in output_file (in PNG format), returning the
    GDAL GeoTransform tuple to use for the image.
    """

    import requests
    from cachecontrol import CacheControl
    from cachecontrol.caches.file_cache import FileCache
    from PIL import Image
    from PIL import ImageFilter
    from cStringIO import StringIO

    url = _UrlPattern(url_pattern)
    tile_size = 256

    session = requests.Session()
    if cache:
        session = CacheControl(session, cache=FileCache(cache))

    topleft = mercator_point_to_coord(zoom, bounds[0], bounds[3])
    bottomright = mercator_point_to_coord(zoom, bounds[2], bounds[1])

    minx = int(topleft.column)
    miny = int(topleft.row)
    maxx = int(bottomright.column)
    maxy = int(bottomright.row)

    width = tile_size * (maxx - minx + 1)
    height = tile_size * (maxy - miny + 1)

    if topleft == bottomright:
        response = session.get(url(topleft))
        assert response.status_code == 200
        io = StringIO(response.content)
        im = Image.open(io)
        assert im.mode == 'P'

    else:
        im = Image.new('RGBA', (width, height))

        for x in xrange(minx, maxx + 1):
            for y in xrange(miny, maxy + 1):
                coord = Coordinate(zoom=zoom, column=x, row=y)
                response = session.get(url(coord))
                assert response.status_code == 200

                io = StringIO(response.content)
                tile = Image.open(io)

                assert tile.mode == 'P'
                assert tile.size == (tile_size, tile_size)
                dx = x - minx
                dy = y - miny
                im.paste(tile, (dx * tile_size, dy * tile_size))

        im = im.quantize()

    im.save(output_file)

    return _geotransform(topleft, bottomright, width, height)


class _tempdir(object):

    def __enter__(self):
        import tempfile
        self.tempdir = tempfile.mkdtemp()
        return self.tempdir

    def __exit__(self, type, value, traceback):
        import shutil
        shutil.rmtree(self.tempdir)


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

    layer = _find_layer(ctx.feature_layers, layer_name)
    features = layer['features']

    with _tempdir() as tmp:
        output_png = path_join(tmp, 'landcover.png')
        geotransform = _download_raster_png(
            ctx.unpadded_bounds, ctx.nominal_zoom, url_pattern,
            output_png, median_filter_size, cache)

        ds = gdal.Open(output_png)
        assert ds is not None

        srs = osr.SpatialReference()
        srs.ImportFromEPSG(3857)
        ds.SetProjection(srs.ExportToWkt())
        ds.SetGeoTransform(geotransform)
        band = ds.GetRasterBand(1)

        ogr_layername = 'layer'
        drv = ogr.GetDriverByName('memory')
        dst_ds = drv.CreateDataSource('')
        ogr_layer = dst_ds.CreateLayer(
            ogr_layername, geom_type=ogr.wkbPolygon, srs=srs)
        field = ogr.FieldDefn('Red', ogr.OFTInteger)
        ogr_layer.CreateField(field)

        gdal.Polygonize(band, None, ogr_layer, 0, [], None)

        palette = band.GetColorTable()
        for feature in ogr_layer:
            colour_index = feature.GetField('Red')
            red = palette.GetColorEntry(colour_index)[0]
            kind_detail = kinds_mapping.get(red)

            if kind_detail:
                ogr_geom = feature.GetGeometryRef()
                shape = wkb_loads(ogr_geom.ExportToWkb())

                props = {'kind': 'landcover', 'kind_detail': kind_detail}
                features.append((shape, props, None))

        # otherwise GDAL won't free any resources!
        ds = None
        dst_ds = None

    return layer
