from os import environ
import requests
import re
import lxml.etree as ET
import time


OVERPASS_SERVER = environ.get('OVERPASS_SERVER', 'overpass-api.de')


def chunks(length, iterable):
    """
    Converts an iterable into a generator of chunks of size up to length.
    """

    chunk = []
    for obj in iterable:
        chunk.append(obj)
        if len(chunk) >= length:
            yield chunk
            del chunk[:]
    if chunk:
        yield chunk


class OsmChange(object):
    def __init__(self, fh):
        self.fh = fh
        self.fh.write("<?xml version='1.0' encoding='utf-8'?>\n")
        self.fh.write("<osmChange version=\"0.6\">\n")

    def flush(self):
        self.fh.write("</osmChange>\n")

    def query_result(self, query):
        retry_count = 4
        wait_time_in_s = 100
        r = None
        for _ in range(retry_count):
            r = requests.get("http://%s/api/interpreter" % OVERPASS_SERVER,
                         params=dict(data=query))
            if r.status_code == 200:
                # "200 OK is sent when the query has been successfully answered.
                # The payload of the response is the result data."
                # quote from http://overpass-api.de/command_line.html
                # so response is usable
                break

            if r.status_code not in (429, 504):
                # "429 Too Many Requests is sent if you pass multiple queries from one IP"
                # regularly happens with multiple sequential querries
                # "504 Gateway Timeout is sent if the server has already so much
                # load that the request cannot be executed. In most cases,
                # it is best to try again later"
                # quotes from http://overpass-api.de/command_line.html

                # in cases of 429 and 504 waiting and retrying is typically enough to get an expected response
                break

            print "%d code returned instead of overpass response - request will be repeated after %d seconds" % (r.status_code, wait_time_in_s)
            time.sleep(wait_time_in_s)

        if r.status_code != 200:
            raise RuntimeError("Unable to fetch data from Overpass: %r"
                               % r.status_code)
        if r.headers['content-type'] != 'application/osm3s+xml':
            raise RuntimeError("Expected XML, but got %r"
                               % r.headers['content-type'])
        return r.content

    def add_query(self, query):
        data = self.query_result(query)
        root = ET.fromstring(data)
        root.tag = 'modify'
        del root.attrib['version']
        del root.attrib['generator']
        root.remove(root.find('note'))
        root.remove(root.find('meta'))
        xml = ET.ElementTree(root)
        xml.write(self.fh, encoding='utf8', xml_declaration=False)


class DataDumper(object):
    def __init__(self):
        self.nodes = set()
        self.ways = set()
        self.relations = set()
        self.pattern = re.compile('#.*(node|way|rel(ation)?)[ /]+([0-9]+)')

        self.raw_queries = list()
        self.raw_pattern = re.compile('#.*RAW QUERY:(.*)')

    def add_object(self, typ, id_str):
        id = int(id_str)
        if typ == 'node':
            self.nodes.add(id)

        elif typ == 'way':
            self.ways.add(id)

        else:
            assert typ.startswith('rel'), \
                "Expected 'rel' or 'relation', got %r" % typ
            self.relations.add(id)

    def add_query(self, raw):
        self.raw_queries.append(raw)

    def build_query(self, fmt, ids):
        query = "("
        for id in ids:
            query += fmt % id
        query += ");out;"
        return query

    def download_to(self, fh):
        osc = OsmChange(fh)

        for n_ids in chunks(1000, self.nodes):
            osc.add_query(self.build_query("node(%d);", n_ids))
        for w_ids in chunks(100, self.ways):
            osc.add_query(self.build_query("way(%d);>;", w_ids))
        for r_ids in chunks(10, self.relations):
            osc.add_query(self.build_query("relation(%d);>;",  r_ids))
        for raw_query in self.raw_queries:
            osc.add_query("(" + raw_query + ");out;")

        osc.flush()

    def dump_data(self, f, log):
        try:
            with open(f) as fh:
                for line in fh:
                    m = self.pattern.search(line)
                    if m:
                        self.add_object(m.group(1), m.group(3))
                    else:
                        m = self.raw_pattern.search(line)
                        if m:
                            self.add_query(m.group(1).rstrip())
        except:
            print>>log, "FAIL: fetching OSM data for %r" % (f,)
            raise


if __name__ == '__main__':
    import sys

    input_file = sys.argv[1]
    output_fh = open(sys.argv[2]) if len(sys.argv) > 2 else sys.stdout

    dumper = DataDumper()
    dumper.dump_data(input_file, sys.stderr)
    dumper.download_to(output_fh)
    output_fh.close()
