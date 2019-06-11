from math import isinf
from math import isnan


def to_float(x):
    """
    Attempts to convert x to a floating point value, first removing some
    common punctuation.

    Returns None if conversion failed, or if the converted value is not
    finite (i.e: NaN or Inf).
    """

    if x is None:
        return None

    if isinstance(x, (str, unicode)):
        # normalize punctuation
        x = x.replace(';', '.').replace(',', '.')

    try:
        value = float(x)
        # although NaN and Inf are, technically, valid floating point values,
        # they're pretty unhelpful when we're expecting finite values. in
        # addition, they can raise unexpected exceptions when being processed
        # by stages in the pipeline which were written with finite valus in
        # mind. we expect that if we encounter them in input data, that's
        # probably a mistake, so we can treat them as missing / invalid.
        if isnan(value) or isinf(value):
            return None

        return value

    except ValueError:
        return None


def calculate_way_area(shape):
    result = 0
    if shape and shape.type in ('MultiPolygon', 'Polygon'):
        result = shape.area
    return result


def get_height_from_props(props):
    height_str = props.get('height')
    if height_str:
        height = to_float(height_str)
        if height is not None:
            return height
    levels_str = props.get('levels')
    if levels_str:
        levels = to_float(levels_str)
        if levels is not None:
            result = max(levels, 1) * 3 + 2
            return result
    if height_str or levels_str:
        return 1e10


def calculate_volume(area, props):
    result = 0
    if area > 0:
        height = get_height_from_props(props)
        if height is not None and height > 0:
            result = area * height
    return result


def calculate_1px_zoom(way_area):
    import math
    # can't take logarithm of zero, and some ways have
    # incredibly tiny areas, down to even zero. also, by z16
    # all features really should be visible, so we clamp the
    # computation at the way area which would result in 16
    # being returned.
    if way_area < 5.704:
        return 16
    else:
        return 17.256 - math.log(way_area) / math.log(4)


def tag_str_to_bool(str_or_none):
    return True if str_or_none in ('yes', 'true') else None


def true_or_none(x):
    return True if x is True else None


def tag_set_and_not_no(x):
    return x is not None and x != 'no'


def is_building(building_tag, building_part_tag):
    result = (tag_set_and_not_no(building_tag) or
              tag_set_and_not_no(building_part_tag))
    return true_or_none(result)


def safe_int(x):
    if x is None:
        return None
    try:
        return int(x)
    except ValueError:
        pass
    return None
