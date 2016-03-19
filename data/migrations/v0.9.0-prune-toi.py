from redis import StrictRedis
from tilequeue.cache import RedisCacheIndex
from tilequeue.config import make_config_from_argparse
from tilequeue.tile import coord_unmarshall_int
import os.path
import sys

cfg_file = '/etc/tilequeue/config.yaml'
if not os.path.exists(cfg_file):
    sys.exit(0)

cfg = make_config_from_argparse(cfg_file)
redis_client = StrictRedis(cfg.redis_host)
cache_index = RedisCacheIndex(redis_client)

tiles_of_interest = cache_index.fetch_tiles_of_interest()

coord_ints_to_remove = set()
for coord_int in tiles_of_interest:
    coord = coord_unmarshall_int(coord_int)
    if coord.zoom > 16:
        coord_ints_to_remove.add(coord_int)

buf = []
batch_size = 100
for coord_int in coord_ints_to_remove:
    buf.append(coord_int)
    if len(buf) == batch_size:
        redis_client.srem(cache_index.cache_set_key, *buf)
        del buf[:]
if buf:
    redis_client.srem(cache_index.cache_set_key, *buf)
