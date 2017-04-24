from collections import namedtuple
import webcolors
import re


# a type to hold an RGB colour, expect RGB integers between 0-255
Colour = namedtuple('Colour', 'r g b')


# matches a regular hex colour with either 6 or 3 hexadecimal digits
HEX6 = re.compile('^#[0-9a-f]{6}$')
HEX3 = re.compile('^#[0-9a-f]{3}$')

# matches a hex6 plus two extra (ignored) digits for alpha
HEX6_PLUS = re.compile('^#[0-9a-f]{6}[0-9a-f]*$')

# matches a hex6 which doesn't have a leading hash
HEX6_NO_HASH = re.compile('^[0-9a-f]{6}$')


def parse_colour(colour):
    """
    Parse a string which represents a colour, returning the Colour value which
    gives its RGB values. Input strings can be hex6 (#ffffff), hex3 (#fff) or
    a colour name.
    """

    # normalise the string
    colour = colour.lower()
    colour = colour.replace(" ", "")

    if HEX6.match(colour) or HEX3.match(colour):
        rgb = webcolors.hex_to_rgb(colour)
    elif HEX6_PLUS.match(colour):
        rgb = webcolors.hex_to_rgb(colour[0:7])
    elif HEX6_NO_HASH.match(colour):
        rgb = webcolors.hex_to_rgb('#' + colour)
    else:
        try:
            rgb = webcolors.name_to_rgb(colour)
        except ValueError:
            return None
    return Colour(*rgb)
