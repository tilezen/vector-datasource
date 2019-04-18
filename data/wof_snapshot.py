from os.path import basename
from os.path import splitext
from os.path import join as path_join
from tilequeue.wof import Neighbourhood
from tilequeue.wof import NeighbourhoodFailure
from tilequeue.wof import NeighbourhoodMeta
from tilequeue.wof import create_neighbourhood_from_json
from tilequeue.wof import write_neighbourhood_data_to_file
import json
import tarfile
import requests
from tqdm import tqdm


def _parse_wof_id(s):
    wof_id, ext = splitext(basename(s))
    assert ext == '.geojson'
    return int(wof_id)


def _parse_neighbourhood(file_name, data, placetype, file_hash):
    wof_id = _parse_wof_id(file_name)
    meta = NeighbourhoodMeta(wof_id, placetype, None, file_hash, None)
    json_data = json.loads(data)
    n = create_neighbourhood_from_json(json_data, meta)
    return n


class WOFArchiveReader(object):
    """
    Collects WOF parsed data items (mostly neighbourhoods) from a series of
    tar.gz "bundles" as distributed by WOF.
    """

    def __init__(self):
        self.wof_items = []

    def add_archive(self, archive, file_hash, count):
        """
        Adds the GeoJSON files in the tar.gz archive to the list of wof_items.

        Displays a progress bar, with count being the expected number of items
        in the tar.gz.
        """

        with tqdm(total=count) as pbar:
            with tarfile.open(archive) as tar:
                for info in tar:
                    if info.isfile() and info.name.endswith('.geojson'):
                        self._parse_file(
                            info.name, tar.extractfile(info).read(), file_hash)
                        pbar.update(1)

    def _parse_file(self, file_name, data, file_hash):
        n_or_fail = _parse_neighbourhood(file_name, data, placetype, file_hash)
        if isinstance(n_or_fail, Neighbourhood):
            self.wof_items.append(n_or_fail)
        elif isinstance(n_or_fail, NeighbourhoodFailure):
            if n_or_fail.skipped or n_or_fail.funky or n_or_fail.superseded:
                pass
            else:
                raise ValueError("Failed to parse neighbourhood: %s "
                                 "(because: %s)"
                                 % (n_or_fail.message, n_or_fail.reason))
        else:
            raise ValueError("Unexpected %r" % (n_or_fail,))


class tmpdownload(object):
    """
    Downloads a file to a temporary location and yields its absolute path. Once
    the scope exits, deletes the temporary file.
    """

    def __init__(self, url, expected_size):
        import tempfile
        self.tempdir = tempfile.mkdtemp()

        fname = url.split('/')[-1]
        abs_fname = path_join(self.tempdir, fname)

        # see https://stackoverflow.com/questions/16694907/#16696317
        with requests.get(url, stream=True) as response:
            response.raise_for_status()

            with tqdm(total=expected_size) as pbar:
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


WOF_INVENTORY = 'https://dist.whosonfirst.org/bundles/inventory.json'
WOF_BUNDLE_PREFIX = 'https://dist.whosonfirst.org/bundles/'


if __name__ == '__main__':
    inventory = requests.get(WOF_INVENTORY).json()
    reader = WOFArchiveReader()

    for placetype in ('neighbourhood', 'macrohood', 'microhood', 'borough'):
        fname = 'whosonfirst-data-%s-latest.tar.bz2' % (placetype,)

        matching = [item for item in inventory
                    if item['name_compressed'] == fname]
        assert len(matching) == 1
        item = matching[0]

        version = item['last_updated']
        count = item['count']
        download_size = item['size_compressed']

        print "Downloading %r with %d entries" % (placetype, count)
        with tmpdownload(WOF_BUNDLE_PREFIX + fname, download_size) as fname:
            print "Parsing WOF data"
            reader.add_archive(fname, version, count)

    print "Writing output SQL"
    with open('wof_snapshot.sql', 'w') as fh:
        fh.write("COPY public.wof_neighbourhood ("
                 "wof_id, placetype, name, hash, n_photos, area, min_zoom, "
                 "max_zoom, is_landuse_aoi, label_position, geometry, "
                 "inception, cessation, is_visible, l10n_name, wikidata) "
                 "FROM stdin;\n")
        write_neighbourhood_data_to_file(fh, reader.wof_items)
        fh.write("\\.\n")
