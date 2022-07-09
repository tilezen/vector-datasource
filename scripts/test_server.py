import os
import sys

from tileserver import create_tileserver_from_config
from werkzeug.debug import DebuggedApplication
from werkzeug.serving import make_server

# command line arguments:
#   1. the database name
#   2. the user to connect as
#   3. the file to create with the port number in it

config = {
    'postgresql': {
        'dbnames': [sys.argv[1]],
        'user': sys.argv[2]
    },
    'queries': {
        'config': 'queries.yaml',
        'template-path': 'queries',
        'reload-templates': False
    },
    'formats': ['json', 'topojson', 'mvt', 'mvtb'],
    'buffer': {
        'mvtb': {
            'layer': {
                'earth': {'point': 256},
                'water': {'point': 256},
                'places': {'point': 128}
            },
            'geometry': {
                'point': 64,
                'line': 8,
                'polygon': 8
            }
        }
    },
    'yaml': {
        'type': 'parse',
        'parse': {
            'path': './yaml',
        },
        'callable': {
            'dotted-name': 'vectordatasource.meta.python.make_function_mapping',
            'args': ['vectordatasource.gen'],
        },
    },
}

tile_server = create_tileserver_from_config(config)
tile_server.propagate_errors = True

application = DebuggedApplication(tile_server, True)

http_server = make_server('localhost', 0, application, threaded=False)
with open(sys.argv[3] + '.tmp', 'w') as fh:
    print>>fh, '%d' % http_server.server_port
# move into place atomically
os.rename(sys.argv[3] + '.tmp', sys.argv[3])

http_server.serve_forever()
