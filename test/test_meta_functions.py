import unittest


class UnitParsingTest(unittest.TestCase):

    def _assert_meters(self, tag_value, expected):
        from vectordatasource.meta.function import mz_to_float_meters
        parsed = mz_to_float_meters(tag_value)

        if parsed is None and expected is not None:
            self.fail("Failed to parse %r, but expected %r."
                      % (tag_value, expected))

        elif parsed is not None and expected is None:
            self.fail("Parsed %r as %r, but expected parsing to fail."
                      % (tag_value, parsed))

        elif parsed != expected and abs(parsed - expected) > 0.001:
            self.fail("Expected %r from %r, but got %r instead."
                      % (expected, tag_value, parsed))

    def test_parse_miles(self):
        self._assert_meters('1mi', 1609.3440)

    def test_parse_kilometers(self):
        self._assert_meters('1km', 1000.0)

    def test_parse_meters(self):
        self._assert_meters('1m', 1.0)

    def test_parse_nautical_miles(self):
        self._assert_meters('1nmi', 1852.0)

    def test_parse_feet(self):
        self._assert_meters('1ft', 0.3048)

    def test_parse_space_variations(self):
        self._assert_meters('1.0 m', 1.0)
        self._assert_meters('10.0m', 10.0)
        self._assert_meters('1 m', 1.0)
        self._assert_meters('1m', 1.0)

    def test_imperial(self):
        self._assert_meters('1\'', 0.3048)
        self._assert_meters('1.5\'', 0.3048 * 1.5)
        self._assert_meters('1\'6"', 0.3048 * 1.5)
        # this is technically allowed by the regex, so it should be parsed
        # properly, but doesn't make any sense.
        self._assert_meters('1.5\'6"', 0.3048 * 2)

    def test_numeric(self):
        # just a number on its own is assumed to be in meters
        self._assert_meters('1234', 1234.0)

    def test_junk_units(self):
        # we shouldn't parse anything that's not a unit that we can convert.
        self._assert_meters('1nm', None)
        self._assert_meters('1foo', None)
        self._assert_meters('1 foo', None)
        self._assert_meters('not 1', None)
        self._assert_meters('1mm', None)

    def test_none(self):
        # missing tags will be passed through as None, so we have to handle
        # that by returning None.
        self._assert_meters(None, None)

    def test_finite(self):
        # should return a finite number or None
        self._assert_meters('NaN', None)
        self._assert_meters('Inf', None)
        self._assert_meters('-Inf', None)


class ToFloatTest(unittest.TestCase):

    def test_finite(self):
        # to_float should return a finite number or None. technically, both
        # Inf and NaN are valid values for floats, but they do strange things
        # and may raise unexpected exceptions during arithmetic. in general,
        # we do not expect to see valid uses of NaN or Inf in input data.
        from vectordatasource.util import to_float
        self.assertIsNone(to_float('NaN'))
        self.assertIsNone(to_float('Inf'))
        self.assertIsNone(to_float('-Inf'))
