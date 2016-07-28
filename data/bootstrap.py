from jinja2 import Environment
from jinja2 import FileSystemLoader
import yaml

with open('assets.yaml') as fh:
    asset_cfg = yaml.load(fh)

dest_prj = asset_cfg.get('prj', 3857)
bucket = asset_cfg['bucket']
datestamp = asset_cfg['datestamp']

template_path = '.'
environment = Environment(loader=FileSystemLoader(template_path))
prepare_data_template = environment.get_template('Makefile-prepare-data.jinja2')

src_shapefile_zips = []
src_shapefile_shps = []
src_shapefile_wildcards = []
shapefiles = []
reproj_shapefile_dep_names = []
reproj_shapefile_tgt_names = []
reproj_shapefiles = []
sameproj_shapefile_zips = []
tgt_shapefile_zips = []
tgt_shapefile_shps = []
tgt_shapefile_wildcards = []
cfg_shapefiles = asset_cfg['shapefiles']

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

    shapefile['src_zip'] = src_zip
    shapefile['src_shp'] = src_shp
    shapefile['src_wildcard'] = src_wildcard
    src_shapefile_zips.append(src_zip)
    src_shapefile_shps.append(src_shp)
    src_shapefile_wildcards.append(src_wildcard)

    if shapefile['prj'] != 3857:
        tgt_zip = src_zip.replace('.zip', '-merc.zip')
        tgt_shp = tgt_zip.replace('.zip', '.shp')
        shapefile['tgt_zip'] = tgt_zip
        shapefile['tgt_shp'] = tgt_shp
        tgt_shp_wildcard = tgt_shp.replace('.shp', '*')
        shapefile['tgt_shp_wildcard'] = tgt_shp_wildcard

        reproj_shapefiles.append(shapefile)
        reproj_shapefile_dep_names.append(src_zip)
        reproj_shapefile_tgt_names.append(tgt_zip)
        tgt_shapefile_zips.append(tgt_zip)
        tgt_shapefile_shps.append(tgt_shp)
        tgt_shapefile_wildcards.append(tgt_shp_wildcard)
    else:
        sameproj_shapefile_zips.append(src_zip)
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

src_shapefile_zips_str = ' '.join(src_shapefile_zips)
reproj_shapefile_dep_names_str = ' '.join(reproj_shapefile_dep_names)
reproj_shapefile_tgt_names_str = ' '.join(reproj_shapefile_tgt_names)
sameproj_shapefile_zips_str = ' '.join(sameproj_shapefile_zips)
tgt_shapefile_zips_str = ' '.join(tgt_shapefile_zips)
tgt_shapefile_shps_str = ' '.join(tgt_shapefile_shps)
tgt_shapefile_wildcards_str = ' '.join(tgt_shapefile_wildcards)
src_shapefile_wildcards_str = ' '.join(src_shapefile_wildcards)
prepare_data_makefile = prepare_data_template.render(
    src_shapefile_zips=src_shapefile_zips_str,
    shapefiles=shapefiles,
    reproj_shapefiles=reproj_shapefiles,
    reproj_shapefile_dep_names=reproj_shapefile_dep_names_str,
    reproj_shapefile_tgt_names=reproj_shapefile_tgt_names_str,
    tgt_shapefile_zips=tgt_shapefile_zips_str,
    tgt_shapefile_shps=tgt_shapefile_shps_str,
    tgt_shapefile_wildcards=tgt_shapefile_wildcards_str,
    src_shapefile_wildcards=src_shapefile_wildcards_str,
    bucket=bucket,
    datestamp=datestamp,
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
