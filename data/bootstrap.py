from jinja2 import Environment
from jinja2 import FileSystemLoader
import yaml
import urllib

with open('assets.yaml') as fh:
    asset_cfg = yaml.load(fh)

dest_prj = asset_cfg.get('prj', 3857)
bucket = asset_cfg['bucket']
datestamp = asset_cfg['datestamp']

template_path = '.'
environment = Environment(loader=FileSystemLoader(template_path))
prepare_data_template = environment.get_template(
    'Makefile-prepare-data.jinja2')

src_shapefile_zips = []
src_shapefile_shps = []
src_shapefile_wildcards = []
shapefiles = []
tile_shapefiles = []
reproj_shapefiles = []
tgt_shapefile_zips = []
tgt_shapefile_shps = []
tgt_shapefile_wildcards = []
cfg_shapefiles = asset_cfg['shapefiles']
cfg_wikidata_queries = asset_cfg['wikidata-queries']

# track these separately, as the same URL/zipfile can contain several sets
# of shapefiles.
urls_to_download = {}

for cfg_shapefile in cfg_shapefiles:
    shapefile = cfg_shapefile.copy()
    src_zip = shapefile['url'].split('/')[-1]

    # in case the name of the shapefile is different than the zip
    shapefile_name = shapefile.get('shapefile-name')
    if shapefile_name is None:
        src_shp = src_zip.replace('.zip', '.shp')
    else:
        src_shp = shapefile_name

    directory = shapefile.get('directory')
    if directory:
        # these are used for removal in clean target
        src_wildcard = directory
        tgt_shapefile_wildcards.append(directory)
    else:
        src_wildcard = src_shp.replace('.shp', '*')

    urls_to_download[src_zip] = shapefile['url']

    shapefile['src_zip'] = src_zip
    shapefile['src_shp'] = src_shp
    shapefile['src_wildcard'] = src_wildcard
    src_shapefile_zips.append(src_zip)
    src_shapefile_shps.append(src_shp)
    src_shapefile_wildcards.append(src_wildcard)

    if shapefile['prj'] != 3857:
        tgt_shp = src_shp.replace('.shp', '-merc.shp')
        tgt_zip = tgt_shp.replace('.shp', '.zip')
        shapefile['tgt_zip'] = tgt_zip
        shapefile['tgt_shp'] = tgt_shp
        tgt_shp_wildcard = tgt_shp.replace('.shp', '*')
        shapefile['tgt_shp_wildcard'] = tgt_shp_wildcard

        reproj_shapefiles.append(shapefile)
        tgt_shapefile_zips.append(tgt_zip)
        tgt_shapefile_shps.append(tgt_shp)
        tgt_shapefile_wildcards.append(tgt_shp_wildcard)

    elif shapefile.get('tile'):
        tgt_shp = src_shp.replace('.shp', '-tiled.shp')
        tgt_zip = tgt_shp.replace('.shp', '.zip')
        shapefile['tgt_zip'] = tgt_zip
        shapefile['tgt_shp'] = tgt_shp
        tgt_shp_wildcard = tgt_shp.replace('.shp', '*')
        shapefile['tgt_shp_wildcard'] = tgt_shp_wildcard

        tile_shapefiles.append(shapefile)
        tgt_shapefile_zips.append(tgt_zip)
        tgt_shapefile_shps.append(tgt_shp)
        tgt_shapefile_wildcards.append(tgt_shp_wildcard)

    else:
        tgt_zip = src_zip
        tgt_shp = src_shp
        shapefile['tgt_zip'] = tgt_zip
        shapefile['tgt_shp'] = tgt_shp
        tgt_shp_wildcard = tgt_shp.replace('.shp', '*')
        shapefile['tgt_shp_wildcard'] = tgt_shp_wildcard
        tgt_shapefile_zips.append(tgt_zip)
        tgt_shapefile_shps.append(tgt_shp)
        tgt_shapefile_wildcards.append(tgt_shp_wildcard)

    shapefiles.append(shapefile)

WIKIDATA_BASE_QUERY = 'https://query.wikidata.org/sparql'
queries = []
for cfg_query in cfg_wikidata_queries:
    url = WIKIDATA_BASE_QUERY + '?' + urllib.urlencode(
        dict(query=cfg_query['query'], format='json'))
    fname = cfg_query['name'] + '.json'
    queries.append(dict(url=url, output_file=fname))

# turn the map into a list of dicts, makes it easier to handle in jinja2
downloads = []
for tgt, url in urls_to_download.iteritems():
    downloads.append(dict(tgt=tgt, url=url))

src_shapefile_zips_str = ' '.join(src_shapefile_zips)
tgt_shapefile_zips_str = ' '.join(tgt_shapefile_zips)
tgt_shapefile_shps_str = ' '.join(tgt_shapefile_shps)
tgt_shapefile_wildcards_str = ' '.join(tgt_shapefile_wildcards)
src_shapefile_wildcards_str = ' '.join(src_shapefile_wildcards)
query_output_files = ' '.join(q['output_file'] for q in queries)
prepare_data_makefile = prepare_data_template.render(
    src_shapefile_zips=src_shapefile_zips_str,
    shapefiles=shapefiles,
    reproj_shapefiles=reproj_shapefiles,
    tile_shapefiles=tile_shapefiles,
    tgt_shapefile_zips=tgt_shapefile_zips_str,
    tgt_shapefile_shps=tgt_shapefile_shps_str,
    tgt_shapefile_wildcards=tgt_shapefile_wildcards_str,
    src_shapefile_wildcards=src_shapefile_wildcards_str,
    bucket=bucket,
    datestamp=datestamp,
    downloads=downloads,
    queries=queries,
    query_output_files=query_output_files,
)
with open('Makefile-prepare-data', 'w') as fh:
    fh.write(prepare_data_makefile)
    fh.write('\n')

import_data_template = environment.get_template('Makefile-import-data.jinja2')
import_data_makefile = import_data_template.render(
    bucket=bucket,
    datestamp=datestamp,
    tgt_shapefile_zips=tgt_shapefile_zips_str,
    tgt_shapefile_shps=tgt_shapefile_shps_str,
    tgt_shapefile_wildcards=tgt_shapefile_wildcards_str,
    src_shapefile_wildcards=src_shapefile_wildcards_str,
    shapefiles=shapefiles,
)
with open('Makefile-import-data', 'w') as fh:
    fh.write(import_data_makefile)
    fh.write('\n')
