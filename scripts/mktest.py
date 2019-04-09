import requests
import xml.etree.ElementTree as ET
import tilequeue.tile as tile
from ModestMaps.Core import Coordinate
import os
from contextlib import contextmanager


def node(node_id, zoom=16):
    url = 'https://api.openstreetmap.org/api/0.6/node/%d' % (node_id,)
    headers = {'user-agent': 'mktest.py/0.0.1 (https://github.com/tilezen)'}
    r = requests.get(url, headers=headers)
    root = ET.fromstring(r.content)
    assert root.tag == 'osm'

    tags = {}
    pos = None

    for child in root:
        if child.tag == 'node':
            lat = float(child.attrib['lat'])
            lon = float(child.attrib['lon'])
            pos = (lon, lat)
            for nchild in child:
                if nchild.tag == 'tag':
                    k = nchild.attrib['k']
                    v = nchild.attrib['v']
                    tags[k] = v
            break

    assert pos
    tags['source'] = 'openstreetmap.org'

    return pos, tags


def way_full(way_id, zoom=16):
    url = 'https://api.openstreetmap.org/api/0.6/way/%d/full' % (way_id,)
    headers = {'user-agent': 'mktest.py/0.0.1 (https://github.com/tilezen)'}
    r = requests.get(url, headers=headers)
    root = ET.fromstring(r.content)
    assert root.tag == 'osm'

    nodes = {}
    nds = []
    tags = {}

    for child in root:
        if child.tag == 'node':
            node_id = int(child.attrib['id'])
            nodes[node_id] = child

        elif child.tag == 'way':
            assert way_id == int(child.attrib['id'])
            for wchild in child:
                if wchild.tag == 'nd':
                    nds.append(int(wchild.attrib['ref']))
                elif wchild.tag == 'tag':
                    k = wchild.attrib['k']
                    v = wchild.attrib['v']
                    tags[k] = v

    assert nds
    first_node = nodes[nds[0]]
    lat = float(first_node.attrib['lat'])
    lon = float(first_node.attrib['lon'])
    x, y = tile.deg2num(lat, lon, zoom)

    tags['source'] = 'openstreetmap.org'

    return Coordinate(zoom=zoom, column=x, row=y), tags


def routes_using(way_id):
    url = 'https://api.openstreetmap.org/api/0.6/way/%d/relations' % (way_id,)
    headers = {'user-agent': 'mktest.py/0.0.1 (https://github.com/tilezen)'}
    r = requests.get(url, headers=headers)
    root = ET.fromstring(r.content)
    assert root.tag == 'osm'

    rel_tags = []

    for relation in root:
        if relation.tag == 'relation':
            tags = {}
            for child in relation:
                if child.tag == 'tag':
                    k = child.attrib['k']
                    v = child.attrib['v']
                    tags[k] = v
            if tags.get('type') == 'route' and \
               tags.get('route') == 'road':
                tags['source'] = 'openstreetmap.org'
                rel_tags.append(tags)

    return rel_tags


def _make_ident(s):
    if isinstance(s, unicode):
        s = s.encode('ascii', 'replace')
    elif isinstance(s, (int, long, bool, float)):
        s = repr(s)
    return s.lower().translate(None, ':-')


def _almost_repr(value):
    # we'd prefer not to have all the u'' stuff everywhere unless it's
    # necessary, so try to see if we can return a plain str, if the string
    # is all ASCII anyway.
    if isinstance(value, unicode):
        try:
            value = value.encode('ascii')
        except UnicodeEncodeError:
            # just use the original
            pass

    return repr(value)


def _render_template(name, args):
    from jinja2 import Environment, FileSystemLoader

    d = os.path.dirname(os.path.realpath(__file__))
    env = Environment(loader=FileSystemLoader(os.path.join(d, 'templates')))
    env.filters['repr'] = _almost_repr
    template = env.get_template('%s.jinja2' % (name,))

    output = template.render(**args)
    return output


def road_test(args):
    import json

    coord, way_tags = way_full(args.way_id, args.zoom)
    rel_tags = routes_using(args.way_id)
    expect = json.loads(args.expect) if args.expect else None

    if expect:
        name = '_'.join(_make_ident(v) for v in expect.values())
    else:
        name = 'FIXME'

    args = dict(
        name=name,
        z=args.zoom,
        x=coord.column,
        y=coord.row,
        way_id=args.way_id,
        iso_code=args.is_in,
        way_tags=way_tags,
        relations=rel_tags,
        expect=expect,
    )

    output = _render_template('road_test', args)
    print output.encode('utf-8')


def node_test(args):
    import json

    position, node_tags = node(args.node_id, args.zoom)
    x, y = tile.deg2num(position[1], position[0], args.zoom)
    coord = Coordinate(zoom=args.zoom, column=x, row=y)
    expect = json.loads(args.expect) if args.expect else None

    if expect:
        name = '_'.join(_make_ident(v) for v in expect.values())
    else:
        name = 'FIXME'

    args = dict(
        name=name,
        z=args.zoom,
        x=coord.column,
        y=coord.row,
        position=position,
        node_id=args.node_id,
        node_tags=node_tags,
        expect=expect,
        layer_name=args.layer_name,
    )

    output = _render_template('node_test', args)
    print output.encode('utf-8')


def _shapefile_iterator(sf, field_names):
    from shapely.geometry import shape as make_shape
    from collections import defaultdict

    fid = 0
    for row in sf.iterShapeRecords():
        shape = make_shape(row.shape.__geo_interface__)
        props = defaultdict(lambda: None)
        for k, v in zip(field_names, row.record):
            if isinstance(v, str):
                v = unicode(v.rstrip(), 'utf-8')
            if v:
                props[k] = v
        yield shape, props, fid
        fid += 1


class tempdir(object):

    def __enter__(self):
        import tempfile
        self.tempdir = tempfile.mkdtemp()
        return self.tempdir

    def __exit__(self, type, value, traceback):
        import shutil
        shutil.rmtree(self.tempdir)


@contextmanager
def _ne_features_from_zip(zipfile):
    from zipfile import ZipFile
    import shapefile

    with ZipFile(zipfile, 'r') as z:
        shpfile = None
        dbffile = None
        for name in z.namelist():
            if name.endswith('.shp'):
                shpfile = name
            elif name.endswith('.dbf'):
                dbffile = name

        if not shpfile:
            raise RuntimeError("Shapefile not found in %r" % (zipfile,))
        if not dbffile:
            raise RuntimeError("DBF file not found in %r" % (zipfile,))

        with tempdir() as tmp:
            # need to extract these to a temp dir because the shapefile
            # reader does seeks on the file object, which the streaming
            # file-like object returned from zip open() doesn't support.
            tmp_shpfile = z.extract(shpfile, tmp)
            tmp_dbffile = z.extract(dbffile, tmp)

            with open(tmp_shpfile, "rb") as shp:
                with open(tmp_dbffile, "rb") as dbf:
                    sf = shapefile.Reader(shp=shp, dbf=dbf)
                    field_names = [f[0].lower() for f in sf.fields[1:]]

                    yield _shapefile_iterator(sf, field_names)


def naturalearth_test(args):
    import json
    from shapely.ops import transform
    from tilequeue.tile import reproject_lnglat_to_mercator

    where = compile(args.where, '<command line arguments>', 'eval')

    feature = None
    with _ne_features_from_zip(args.zip) as features:
        for shape, props, fid in features:
            if eval(where, {}, props):
                feature = (shape, props, fid)
                break

    if not feature:
        raise RuntimeError("Unable to find item in NE zip %r matching %r"
                           % (args.zip, args.where))

    expect = json.loads(args.expect) if args.expect else None

    if expect:
        name = '_'.join(_make_ident(v) for v in expect.values())
    else:
        name = 'FIXME'

    if shape.geom_type in ('Point', 'Multipoint'):
        geom_func = 'tile_centre_shape'
        geom_extra_args = ''
        lon, lat = shape.coords[0]

    elif shape.geom_type in ('Polygon', 'MultiPolygon'):
        shape_merc = transform(reproject_lnglat_to_mercator, shape)
        geom_func = 'box_area'
        geom_extra_args = ', %f' % (shape_merc.area,)
        lon, lat = shape.representative_point().coords[0]

    else:
        raise RuntimeError("Haven't implemented NE shape type %r yet."
                           % (shape.geom_type,))

    # check that lon & lat are within expected range. helps to catch shape
    # files which have been projected to mercator.
    assert -90 <= lat <= 90
    assert -180 <= lon <= 180

    x, y = tile.deg2num(lat, lon, args.zoom)
    coord = Coordinate(zoom=args.zoom, column=x, row=y)

    props['source'] = 'naturalearthdata.com'

    args = dict(
        name=name,
        z=args.zoom,
        x=coord.column,
        y=coord.row,
        geom_func=geom_func,
        ne_id=args.ne_id,
        iso_code=args.is_in,
        props=props,
        expect=expect,
        layer_name=args.layer_name,
        geom_extra_args=geom_extra_args,
    )

    output = _render_template('naturalearth_test', args)
    print output.encode('utf-8')


def _overpass_api(query):
    import json

    overpass_api = 'https://overpass-api.de/api/interpreter'
    data = '[out:json][timeout:5][maxsize:1048576];' \
           '%s;out 1 geom qt;' % (query,)
    r = requests.get(overpass_api, params=dict(data=data))

    response = json.loads(r.text)
    return response["elements"]


def _overpass_fetch(element_type, bbox, query):
    return _overpass_api(
        '(%s[%s](%s);)' % (element_type, query, ','.join(str(f) for f in bbox))
    )


def _overpass_fetch_id(element_type, element_id):
    return _overpass_api('(%s(%d);)' % (element_type, element_id))


def _overpass_find(element_type, query):
    # note: all this arithmetic is on (lat, lon) pairs because that's the
    # (incorrect) order that Overpass expects it to be in.

    if query.startswith('id:'):
        elements = _overpass_fetch_id(element_type, int(query[3:]))
        return elements[0]

    centre = (40.82580725925, -73.9098083973)
    size = (0.17457992415, 0.1867675781)
    factor = 1.0
    max_factor = max(90 / size[0], 180 / size[1])

    while factor < max_factor:
        # don't use the full latitude range, as we can't express that in
        # mercator tile coordinates!
        bbox = [max(-85, centre[0] - factor * size[0]),
                max(-180, centre[1] - factor * size[1]),
                min(85, centre[0] + factor * size[0]),
                min(180, centre[1] + factor * size[1])]

        elements = _overpass_fetch(element_type, bbox, query)
        if elements:
            break

        factor = factor * 2.0

    else:
        raise RuntimeError("Nothing matching %r found!" % (query,))

    return elements[0]


class _OverpassNode(object):
    def __init__(self, query):
        element = _overpass_find('node', query)
        self.position = tuple(element[p] for p in ('lat', 'lon'))
        self.element_id = element['id']
        self.tags = element['tags']

    def element_type(self):
        return 'node'

    def geom_fn_name(self):
        return 'dsl.point'

    def geom_fn_arg(self):
        lat, lon = self.position
        return "(%f, %f)" % (lon, lat)


class _OverpassWay(object):
    def __init__(self, query):
        element = _overpass_find('way', query)
        point = element['geometry'][0]
        self.position = tuple(point[p] for p in ('lat', 'lon'))
        self.element_id = element['id']
        self.tags = element.get('tags', {})

    def element_type(self):
        return 'way'

    def geom_fn_name(self):
        return 'dsl.way'


class _OverpassWayArea(object):
    def __init__(self, query):
        from shapely.geometry import Polygon
        from shapely.ops import transform
        from tilequeue.tile import reproject_lnglat_to_mercator
        from tilequeue.tile import reproject_mercator_to_lnglat

        element = _overpass_find('way', query)

        ring = tuple((p['lon'], p['lat']) for p in element['geometry'])
        poly = Polygon(ring)
        poly_merc = transform(reproject_lnglat_to_mercator, poly)

        point = poly_merc.centroid
        lng, lat = reproject_mercator_to_lnglat(point.x, point.y)

        self.position = (lat, lng)
        self.element_id = element['id']
        self.tags = element.get('tags', {})
        self.area = poly_merc.area

    def element_type(self):
        return 'way'

    def geom_fn_name(self):
        return 'dsl.way'

    def geom_fn_arg(self):
        return 'dsl.box_area(z, x, y, %d)' % (int(self.area),)


class _OverpassWayLine(_OverpassWay):
    def __init__(self, query):
        super(_OverpassWayLine, self).__init__(query)

    def geom_fn_arg(self):
        return 'dsl.tile_diagonal(z, x, y)'


class _OverpassRel(object):
    def __init__(self, query):
        from shapely.ops import polygonize
        from shapely.ops import transform
        from tilequeue.tile import reproject_lnglat_to_mercator
        from tilequeue.tile import reproject_mercator_to_lnglat

        element = _overpass_find('relation', query)
        assert element['members']
        total_area = 0
        largest_area = 0
        point = None

        lines = []
        for m in element['members']:
            lines.append(tuple((p['lon'], p['lat']) for p in m['geometry']))

        for poly in polygonize(lines):
            poly_merc = transform(reproject_lnglat_to_mercator, poly)
            area = poly_merc.area
            total_area += area
            if area > largest_area:
                largest_area = area
                point = poly_merc.centroid

        assert point
        assert largest_area > 0

        lng, lat = reproject_mercator_to_lnglat(point.x, point.y)
        self.position = (lat, lng)
        self.element_id = element['id']
        self.tags = element.get('tags', {})
        self.area = total_area

    def element_type(self):
        return 'relation'

    def geom_fn_name(self):
        return 'dsl.way'

    def geom_fn_arg(self):
        return 'dsl.box_area(z, x, y, %d)' % (int(self.area),)


def _overpass_element(layer_name, query_fn, args):
    import json

    result = query_fn(args.query)
    pos = result.position
    x, y = tile.deg2num(pos[0], pos[1], args.zoom)
    coord = Coordinate(zoom=args.zoom, column=x, row=y)
    expect = json.loads(args.expect) if args.expect else None

    if expect:
        name = '_'.join(_make_ident(v) for v in expect.values())
    else:
        name = 'FIXME'
    name = name + '_' + result.element_type()

    tags = result.tags
    tags['source'] = 'openstreetmap.org'

    params = dict(
        name=name,
        z=args.zoom,
        x=coord.column,
        y=coord.row,
        elt_id=result.element_id,
        tags=tags,
        expect=expect,
        layer_name=layer_name,
        geom_fn_name=result.geom_fn_name(),
        geom_fn_arg=result.geom_fn_arg(),
        elt_type=result.element_type(),
    )

    output = _render_template('overpass_test', params)
    print output.encode('utf-8')


def overpass_test(args):
    if args.poi:
        _overpass_element('pois', _OverpassNode, args)

    if args.poi_poly:
        _overpass_element('pois', _OverpassWayArea, args)

    if args.poi_poly_rel:
        _overpass_element('pois', _OverpassRel, args)

    if args.landuse:
        _overpass_element('landuse', _OverpassWayArea, args)

    if args.landuse_line:
        _overpass_element('landuse', _OverpassWayLine, args)

    if args.landuse_label:
        _overpass_element('landuse', _OverpassNode, args)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(prog='mktest.py')
    subparsers = parser.add_subparsers(help='sub-command help')

    # ROADS
    road_test_parser = subparsers.add_parser(
        'road', help='make a unit test for a road')

    road_test_parser.add_argument(
        '--way-id', type=int, required=True,
        help='Way ID of the road to use to create the test.')
    road_test_parser.add_argument(
        '--is-in', help='ISO code for country.')
    road_test_parser.add_argument(
        '--expect',
        help='JSON-encoded dict of expected properties.')
    road_test_parser.add_argument(
        '--zoom', type=int, default=16,
        help='Zoom to use for tile.')
    road_test_parser.set_defaults(func=road_test)

    # NODE (places / pois)
    node_test_parser = subparsers.add_parser(
        'node', help='make a unit test for a point from an OSM node.')

    node_test_parser.add_argument(
        '--node-id', type=int, required=True,
        help='Node ID of the OSM element used to create the test.')
    node_test_parser.add_argument(
        '--expect',
        help='JSON-encoded dict of expected properties.')
    node_test_parser.add_argument(
        '--zoom', type=int, default=16,
        help='Zoom to use for tile.')
    node_test_parser.add_argument(
        '--layer-name', default='places',
        help='Name of the layer in the tile to expect this feature in.')
    node_test_parser.set_defaults(func=node_test)

    # NATURAL EARTH
    ne_test_parser = subparsers.add_parser(
        'naturalearth', help='make a unit test using Natural Earth data')

    ne_test_parser.add_argument(
        '--zip', required=True,
        help='Path to NE data .zip to use to create the test.')
    ne_test_parser.add_argument(
        '--where', required=True,
        help='The first data item for which this Python expression returns'
        ' true will be used to create the test.')
    ne_test_parser.add_argument(
        '--is-in', help='ISO code for country.')
    ne_test_parser.add_argument(
        '--expect',
        help='JSON-encoded dict of expected properties.')
    ne_test_parser.add_argument(
        '--zoom', type=int, default=16,
        help='Zoom to use for tile.')
    ne_test_parser.add_argument(
        '--ne-id', type=int, default=1,
        help='Natural Earth ID to use.')
    ne_test_parser.add_argument(
        '--layer-name', default='places',
        help='Name of the layer in the tile to expect this feature in.')
    ne_test_parser.set_defaults(func=naturalearth_test)

    # FIND BY TAGS IN OVERPASS
    overpass_parser = subparsers.add_parser(
        'overpass', help='Use Overpass API to find examples based on tags')

    overpass_parser.add_argument(
        '--query', required=True,
        help='Query to send to Overpass')
    overpass_parser.add_argument(
        '--poi', action='store_true', help='Make a test for a point in the '
        'pois layer.')
    overpass_parser.add_argument(
        '--landuse', action='store_true', help='Make a test for a polygon in '
        'the landuse layer.')
    overpass_parser.add_argument(
        '--landuse-line', action='store_true', help='Make a test for a line '
        'in the landuse layer.')
    overpass_parser.add_argument(
        '--poi-poly', action='store_true', help='Make a test for a POI point '
        'from a polygon centroid.')
    overpass_parser.add_argument(
        '--landuse-label', action='store_true', help='Make a test for a point '
        'in the landuse layer from a node.')
    overpass_parser.add_argument(
        '--poi-poly-rel', action='store_true', help='Make a test for a POI '
        'multipolygon relation.')
    overpass_parser.add_argument(
        '--expect',
        help='JSON-encoded dict of expected properties.')
    overpass_parser.add_argument(
        '--zoom', type=int, default=16,
        help='Zoom to use for tile.')
    overpass_parser.set_defaults(func=overpass_test)

    args = parser.parse_args()
    args.func(args)
