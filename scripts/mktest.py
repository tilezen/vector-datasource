import requests
import xml.etree.ElementTree as ET
import tilequeue.tile as tile
from ModestMaps.Core import Coordinate
from jinja2 import Template
import os
from contextlib import contextmanager


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
    return s.lower().translate(None, ':-')


def _render_template(name, args):
    d = os.path.dirname(os.path.realpath(__file__))
    template_file = os.path.join(d, 'templates', '%s.jinja2' % (name,))
    with open(template_file) as fh:
        template = Template(fh.read())

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


def _shapefile_iterator(sf, field_names):
    from shapely.geometry import shape as make_shape

    fid = 0
    for row in sf.iterShapeRecords():
        shape = make_shape(row.shape.__geo_interface__)
        props = {}
        for k, v in zip(field_names, row.record):
            if isinstance(v, str):
                v = unicode(v.rstrip(), 'utf-8')
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
        lon, lat = shape.coords[0]

    else:
        raise RuntimeError("Haven't implemented NE shape type %r yet."
                           % (shape.geom_type,))

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
    )

    output = _render_template('naturalearth_test', args)
    print output.encode('utf-8')


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
        '--layer-name', default='pois',
        help='Name of the layer in the tile to expect this feature in.')
    ne_test_parser.set_defaults(func=naturalearth_test)

    args = parser.parse_args()
    args.func(args)
