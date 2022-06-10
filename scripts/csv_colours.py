import csv
import sys
from optparse import OptionParser

import yaml

from vectordatasource.colour import parse_colour
from vectordatasource.transform import Palette


def to_hex(colour):
    return '#%02x%02x%02x' % tuple(colour)


yaml_config_file = None
output_file = sys.stdout
output_colour_key = 'Colour name'
input_colour_key = 'colour'

parser = OptionParser()
parser.add_option('-c', '--config', dest='config',
                  help='YAML configuration file to read')
parser.add_option('-o', '--output', dest='output',
                  help='Output file. Default is stdout.')
parser.add_option('-k', '--key', dest='colour_key',
                  help='Key / CSV header to use for output colour.')
parser.add_option('-i', '--input-key', dest='input_colour_key',
                  help='Key / CSV header to use for input colour.')
parser.add_option('-x', '--output-hex-key', dest='output_hex_key',
                  help='Optional key to output hex colour in addition to name')
(options, args) = parser.parse_args()

if options.output:
    output_file = open(options.output, 'wb')

with open(options.config, 'rb') as yaml_fh:
    config = yaml.load(yaml_fh)

if options.colour_key:
    output_colour_key = options.colour_key

palette = Palette(config['colours'])

for file_name in args:
    with open(file_name, 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        writer = None

        for row in reader:
            if writer is None:
                keys = list(row.keys()) + [output_colour_key]
                if options.output_hex_key:
                    keys.append(options.output_hex_key)
                writer = csv.DictWriter(output_file, keys)
                writer.writeheader()
            colour = parse_colour(row[input_colour_key])
            if colour:
                c = palette(colour)
                row[output_colour_key] = c
                if options.output_hex_key:
                    row[options.output_hex_key] = to_hex(palette.get(c))
            writer.writerow(row)
