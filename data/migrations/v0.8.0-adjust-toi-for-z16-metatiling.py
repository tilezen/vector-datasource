from redis import StrictRedis
from tilequeue.cache import RedisCacheIndex
from tilequeue.config import make_config_from_argparse
from tilequeue.tile import coord_marshall_int
from tilequeue.tile import coord_unmarshall_int
import sys

if len(sys.argv) > 1:
    cfg_path = sys.argv[1]
else:
    cfg_path = '/etc/tilequeue/config.yaml'

cfg = make_config_from_argparse(cfg_path)
redis_client = StrictRedis(cfg.redis_host)
cache_index = RedisCacheIndex(redis_client)
tiles_of_interest = cache_index.fetch_tiles_of_interest()

coord_ints_to_add = set()
for coord_int in tiles_of_interest:
    coord = coord_unmarshall_int(coord_int)
    if coord.zoom > 16:
        coord_at_z16 = coord.zoomTo(16).container()
        coord_int_at_z16 = coord_marshall_int(coord_at_z16)
        coord_ints_to_add.add(coord_int_at_z16)

batch_size = 100
buf = []
for coord_int in coord_ints_to_add:
    buf.append(coord_int)
    if len(buf) >= batch_size:
        redis_client.sadd(cache_index.cache_set_key, *buf)
        del buf[:]
if buf:
    redis_client.sadd(cache_index.cache_set_key, *buf)
