import fileinput

from boto import connect_s3
from boto.s3.bucket import Bucket
from tilequeue.tile import deserialize_coord
from tilequeue.tile import serialize_coord


bucket_name = 'mapzen-tiles-assets'
key_name = 'test/integration-test-coords.txt'


coords_to_store = set()
for line in fileinput.input():
    coord = deserialize_coord(line.strip())
    assert coord
    if coord.zoom == 0:
        uplifted_coord = coord
    else:
        uplifted_coord = coord.zoomBy(-1).container()
    coords_to_store.add(uplifted_coord)

sorted_coords = sorted(coords_to_store)
coords_str = '\n'.join(map(serialize_coord, sorted_coords))

conn = connect_s3()
bucket = Bucket(conn, bucket_name)
key = bucket.new_key(key_name)
key.set_contents_from_string(
    coords_str,
    headers={'Content-Type': 'text/plain'},
)
