# -*- coding: utf-8 -*-
import unittest


class ColourParsingTest(unittest.TestCase):

    def test_colour_parse(self):
        from vectordatasource.colour import parse_colour, Colour

        # first, some easy colours which match exactly what we'd expect,
        # they're valid web colour specs.
        self.assertEquals(parse_colour('black'), Colour(0, 0, 0))
        self.assertEquals(parse_colour('white'), Colour(255, 255, 255))
        self.assertEquals(parse_colour('#000000'), Colour(0, 0, 0))
        self.assertEquals(parse_colour('#ffffff'), Colour(255, 255, 255))
        self.assertEquals(parse_colour('#000'), Colour(0, 0, 0))
        self.assertEquals(parse_colour('#fff'), Colour(255, 255, 255))

        # now try some variants on those...
        # hex6 + alpha
        self.assertEquals(parse_colour('#00000000'), Colour(0, 0, 0))
        self.assertEquals(parse_colour('#ffffffff'), Colour(255, 255, 255))
        # hex6 without leading hash
        self.assertEquals(parse_colour('000000'), Colour(0, 0, 0))
        self.assertEquals(parse_colour('ffffff'), Colour(255, 255, 255))
        # uppercase variants
        self.assertEquals(parse_colour('BLACK'), Colour(0, 0, 0))
        self.assertEquals(parse_colour('White'), Colour(255, 255, 255))
        self.assertEquals(parse_colour('#FFFFFF'), Colour(255, 255, 255))
        self.assertEquals(parse_colour('#FFF'), Colour(255, 255, 255))

        # check some common colours
        self.assertEquals(parse_colour('red'), Colour(255, 0, 0))
        self.assertEquals(parse_colour('green'), Colour(0, 128, 0))
        self.assertEquals(parse_colour('blue'), Colour(0, 0, 255))
        self.assertEquals(parse_colour('goldenrod'), Colour(218, 165, 32))

        # check that we get None for errors
        self.assertEquals(parse_colour('thisisnotacolour'), None)

        # check that whitespace in names is removed
        self.assertEquals(
            parse_colour('Dark Sea Green'), Colour(143, 188, 143))
