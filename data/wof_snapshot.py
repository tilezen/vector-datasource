import json
from os.path import basename
from os.path import join as path_join
from os.path import splitext

import requests
from tilequeue.wof import create_neighbourhood_from_json
from tilequeue.wof import Neighbourhood
from tilequeue.wof import NeighbourhoodFailure
from tilequeue.wof import NeighbourhoodMeta
from tilequeue.wof import write_neighbourhood_data_to_file
from tqdm import tqdm


def _parse_wof_id(s):
    """
        expects input to look like "123456.geojson"
    """
    wof_id, ext = splitext(basename(s))
    assert ext == '.geojson'
    return int(wof_id)


def _parse_neighbourhood(file_name, data, placetype, file_hash):
    wof_id = _parse_wof_id(file_name)
    meta = NeighbourhoodMeta(wof_id, placetype, None, file_hash, None)
    json_data = json.loads(data)
    n = create_neighbourhood_from_json(json_data, meta)
    return n


def _parse_neighbourhood_from_json(json_str):
    j = json.loads(json_str)
    wof_id = j['id']
    placetype = j['properties']['wof:placetype']
    meta = NeighbourhoodMeta(wof_id, placetype, None, '123', None)
    hood = create_neighbourhood_from_json(j, meta)
    return hood


class WOFArchiveReader(object):
    """
    Collects WOF parsed data items (mostly neighbourhoods) from a series of
    tar.gz "bundles" as distributed by WOF.
    """

    def __init__(self):
        self.wof_items = []

    def handle_neighborhood_or_fail(self, n_or_fail):
        if isinstance(n_or_fail, Neighbourhood):
            self.wof_items.append(n_or_fail)
        elif isinstance(n_or_fail, NeighbourhoodFailure):
            if n_or_fail.skipped or n_or_fail.funky or n_or_fail.superseded:
                pass
            else:
                raise ValueError('Failed to parse neighbourhood: %s '
                                 '(because: %s)'
                                 % (n_or_fail.message, n_or_fail.reason))
        else:
            raise ValueError('Unexpected %r' % (n_or_fail,))

    def add_sqlite_file(self, sqlite_filename, file_hash):
        with tqdm(desc='Grabbing rows from sqlite file %s' % sqlite_filename, unit='Rows', unit_scale=True) as pbar:
            import sqlite3
            from _sqlite3 import Error
            try:
                conn = sqlite3.connect(sqlite_filename)
                pbar.update(1)
            except Error as e:
                print(e)

            cursor = conn.cursor()
            pbar.update(1)
            query = """
                    select geojson.body from geojson where geojson.id in (
                    select spr.id from spr
                    where spr.placetype IN ('neighbourhood', 'borough','macrohood', 'microhood')
                    AND spr.id != 1
                    AND spr.is_deprecated = 0
                    AND spr.is_superseded = 0
                    AND spr.is_current != 0
                    ) AND geojson.is_alt = 0
                    """
            cursor.execute(query)
            pbar.update(1)

            for row in cursor:
                n_or_fail = _parse_neighbourhood_from_json(row[0])
                self.handle_neighborhood_or_fail(n_or_fail)
                pbar.update(1)


class tmpdownload(object):
    """
    Downloads a file to a temporary location and yields its absolute path. Once
    the scope exits, deletes the temporary file.
    """

    def __init__(self, url):
        import tempfile
        self.tempdir = tempfile.mkdtemp()

        fname = url.split('/')[-1]
        abs_fname = path_join(self.tempdir, fname)

        # see https://stackoverflow.com/questions/16694907/#16696317
        with requests.get(url, stream=True) as response:
            response.raise_for_status()

            with tqdm(desc='Downloading %s' % url, unit='bytes', unit_scale=True) as pbar:
                with open(abs_fname, 'wb') as fh:
                    for chunk in response.iter_content(chunk_size=16384):
                        if chunk:
                            fh.write(chunk)
                            pbar.update(len(chunk))

        self.abs_fname = abs_fname

    def __enter__(self):
        return self.abs_fname

    def __exit__(self, type, value, traceback):
        import shutil
        shutil.rmtree(self.tempdir)


class TmpBz2Decompress(object):
    def __init__(self, filename):
        import bz2
        suffix_length = len('.bz2')
        input_filename = filename[:filename.rfind('/')+1]
        output_filename = filename[:-suffix_length]
        with tqdm(desc='Decompressing %s' % input_filename, unit='bytes', unit_scale=True) as pbar:
            with open(output_filename, 'w') as outfile:
                with bz2.BZ2File(filename, 'r') as bzfile:
                    for chunk in bzfile:
                        outfile.write(chunk)
                        pbar.update(len(chunk))

        self.abs_fname = output_filename

    def __enter__(self):
        return self.abs_fname

    def __exit__(self, type, value, traceback):
        import os
        os.remove(self.abs_fname)


WOF_SQLITE = 'https://data.geocode.earth/wof/dist/sqlite/whosonfirst-data-admin-latest.db.bz2'

if __name__ == '__main__':
    reader = WOFArchiveReader()

    with tmpdownload(WOF_SQLITE) as fname:
        with TmpBz2Decompress(fname) as decompressed:
            reader.add_sqlite_file(decompressed, 'latest')

    print 'Writing output SQL'
    with open('wof_snapshot.sql', 'w') as fh:
        fh.write('COPY public.wof_neighbourhood ('
                 'wof_id, placetype, name, hash, n_photos, area, min_zoom, '
                 'max_zoom, is_landuse_aoi, label_position, geometry, '
                 'inception, cessation, is_visible, l10n_name, wikidata) '
                 'FROM stdin;\n')
        write_neighbourhood_data_to_file(fh, reader.wof_items)
        fh.write('\\.\n')
