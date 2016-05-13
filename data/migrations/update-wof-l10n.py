# This expects a local checkout of whos on first data. It will fetch
# the data from the on disk location for all existing neighbourhoods
# in the database, and generate updates for all neighbourhoods that
# have other local names.

from tilequeue.wof import make_wof_filesystem_neighbourhood_fetcher
from tilequeue.wof import make_wof_model
import os
import sys
import yaml

cfg_path = '/etc/tilequeue/config.yaml'
wof_path = '/var/whosonfirst-data'

if not os.path.exists(cfg_path):
    print 'No tilequeue config found. Not updating wof l10n.'
    sys.exit(0)

if not os.path.exists(wof_path):
    print 'No woftilequeue data found. Not updating wof l10n.'
    sys.exit(1)

with open(cfg_path) as fh:
    yaml_data = yaml.load(fh)

wof_cfg = yaml_data['wof']
psql_cfg = wof_cfg['postgresql']

wof_model = make_wof_model(psql_cfg)
metas = wof_model.find_previous_neighbourhood_meta()
n_threads = 50
fs_neighbourhood_fetcher = make_wof_filesystem_neighbourhood_fetcher(
    wof_path, n_threads)
ns, failures = fs_neighbourhood_fetcher.fetch_raw_neighbourhoods(metas)
if failures:
    print 'Errors fetching neighbourhoods'
    # if there are more than 10, the rest will probably have failed
    # for the same reason
    for failure in failures[:10]:
        print 'Failed fetching %d: %r - %r' % (
            failure.wof_id, failure.reason, failure.message_one_line)
    sys.exit(1)

ns_to_update = []
for n in ns:
    if n.l10n_names:
        ns_to_update.append(n)

ns_to_add = []
ids_to_remove = []
wof_model.sync_neighbourhoods(ns_to_add, ns_to_update, ids_to_remove)
