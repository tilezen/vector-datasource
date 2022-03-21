from . import FixtureTest


def _url_for(osm_id):
    typ = 'way' if osm_id >= 0 else 'relation'
    return 'https://www.openstreetmap.org/%s/%d' % (typ, abs(osm_id))


class BigBoxStores(FixtureTest):

    def test_big_box_stores(self):
        tests = [
            # there are TWO Target stores in this tile - and both are huge!
            ['14/2618/6338', set([152722810, 56149856]), 'department_store'],
            ['14/2620/6333', 219072560, 'supermarket'],
            ['14/2618/6338', 344057345, 'supermarket'],
            ['14/2621/6334', 259001360, 'doityourself'],
            ['15/5240/12668', 194906343, 'supermarket'],
            ['15/5236/12666', -3585039, 'supermarket'],
        ]

        for zxy, osm_ids, kind in tests:
            self._run_test(zxy, osm_ids, kind)

    def _run_test(self, zxy, osm_ids, kind):
        z, x, y = map(int, zxy.split('/'))
        urls = []
        if isinstance(osm_ids, set):
            for osm_id in osm_ids:
                urls.append(_url_for(osm_id))
        else:
            urls.append(_url_for(osm_ids))

        self.load_fixtures(urls, clip=self.tile_bbox(z, x, y))

        self.assert_has_feature(
            z, x, y, 'pois', {'kind': kind, 'id': osm_ids})
