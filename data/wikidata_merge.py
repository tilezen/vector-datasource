import json
from collections import defaultdict


def parse_wikidata(key, input_file):
    with open(input_file, 'rb') as fh:
        data = json.load(fh)

    wikidata = defaultdict(dict)
    for row in data['results']['bindings']:
        wikidata_id = row[key]['value']

        prefix = 'http://www.wikidata.org/entity/'
        assert wikidata_id.startswith(prefix)
        wikidata_id = wikidata_id[len(prefix):]

        for k in row.keys():
            if k != key:
                wikidata[wikidata_id][k] = row[k]['value']

    return wikidata


def wikidata_merge(data, update):
    """
    Updates wikidata records in `data` with new records in `update`.
    """

    for wikidata_id, props in update.iteritems():
        for k, v in props.iteritems():
            data[wikidata_id][k] = v


def write_wikidata_sql(io, data):
    """
    Write wikidata table and data to io.
    """

    io.write("""
DROP TABLE IF EXISTS wikidata;
CREATE TABLE wikidata (id TEXT PRIMARY KEY, tags HSTORE);

COPY wikidata(id, tags) FROM stdin;
""")

    def esc(s):
        s = s.encode('utf-8').replace('\t', ' ').replace('\n', ' ')
        if ' ' in s:
            s = s.replace('"', '\\\\"')
            s = '"%s"' % s
        return s

    for wikidata_id, props in data.iteritems():
        hstore = ','.join(
            "%s=>%s" % (esc(k), esc(v))
            for k, v in props.iteritems())
        io.write("%s\t%s\n" % (wikidata_id, hstore))

    io.write("\\.\n")


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--output', help='Output SQL file')
    parser.add_argument('--key', default='item', help='Wikidata ID key in '
                        'Wikidata query result binding')
    parser.add_argument('input_files', nargs='+', help='Input JSON files '
                        'from Wikidata query')
    args = parser.parse_args()

    wikidata = defaultdict(dict)
    for input_file in args.input_files:
        wikidata_merge(wikidata, parse_wikidata(args.key, input_file))

    with open(args.output, 'w') as fh:
        write_wikidata_sql(fh, wikidata)
