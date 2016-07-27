from jinja2 import Environment
from jinja2 import FileSystemLoader
import yaml

with open('assets.yaml') as fh:
    asset_cfg = yaml.load(fh)

dest_prj = asset_cfg.get('prj', 3857)
bucket = asset_cfg['bucket']

template_path = '.'
environment = Environment(loader=FileSystemLoader(template_path))
template = environment.get_template('Makefile-prepare-data.jinja2')

shapefile_zips = []
shapefiles = []
reproj_shapefile_dep_names = []
reproj_shapefile_tgt_names = []
reproj_shapefiles = []
sameproj_shapefile_zips = []
cfg_shapefiles = asset_cfg['shapefiles']
for cfg_shapefile in cfg_shapefiles:
    shapefile = cfg_shapefile.copy()
    name_zip = shapefile['url'].split('/')[-1]
    shapefile_name = shapefile.get('shapefile-name')
    if shapefile_name is None:
        shapefile['name_shp'] = name_shp = name_zip.replace('.zip', '.shp')
    else:
        shapefile['name_shp'] = name_shp = shapefile_name
    name_shp = name_zip.replace('.zip', '.shp')
    shapefile['name_zip'] = name_zip
    if shapefile['prj'] != 3857:
        reproj_zip = name_zip.replace('.zip', '-merc.zip')
        reproj_shp = name_shp.replace('.shp', '-merc.shp')
        shapefile['reproj_zip'] = reproj_zip
        shapefile['reproj_shp'] = reproj_shp
        shapefile['reproj_shp_wildcard'] = reproj_shp.replace('.shp', '.*')

        reproj_shapefiles.append(shapefile)
        reproj_shapefile_dep_names.append(name_zip)
        reproj_shapefile_tgt_names.append(reproj_zip)
    else:
        sameproj_shapefile_zips.append(name_zip)

    shapefiles.append(shapefile)
    shapefile_zips.append(name_zip)

shapefile_zips_str = ' '.join(shapefile_zips)
reproj_shapefile_dep_names_str = ' '.join(reproj_shapefile_dep_names)
reproj_shapefile_tgt_names_str = ' '.join(reproj_shapefile_tgt_names)
sameproj_shapefile_zips_str = ' '.join(sameproj_shapefile_zips)
proc_shapefile_zips_str = '%s %s' % (
    sameproj_shapefile_zips_str, reproj_shapefile_tgt_names_str)
result = template.render(
    shapefile_zips=shapefile_zips_str,
    shapefiles=shapefiles,
    reproj_shapefiles=reproj_shapefiles,
    reproj_shapefile_dep_names=reproj_shapefile_dep_names_str,
    reproj_shapefile_tgt_names=reproj_shapefile_tgt_names_str,
    proc_shapefile_zips=proc_shapefile_zips_str,
    bucket=bucket,
)
with open('Makefile-prepare-data', 'w') as fh:
    fh.write(result)
    fh.write('\n')
