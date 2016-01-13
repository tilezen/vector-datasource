from shapely.geometry import shape

# this is mid way along the High Line in NYC, which is a huge long
# "building". we should be clipping it to a buffer of 3x the tile
# dimensions.
with features_in_tile_layer(19, 154366, 197054, 'buildings') as buildings:
    # max width and height in degress as 3x the size of the above tile
    max_w = 0.002060
    max_h = 0.001561

    # need to check that we at least saw the high line
    saw_the_high_line = False

    for building in buildings:
        bounds = shape(building['geometry']).bounds
        w = bounds[2] - bounds[0]
        h = bounds[3] - bounds[1]

        if building['properties']['id'] == 37054313:
            saw_the_high_line = True

        if w > max_w or h > max_h:
            raise Exception("feature %r is %rx%r, larger than the allowed "
                            "%rx%r."
                            % (building['properties']['id'],
                               w, h, max_w, max_h))

    if not saw_the_high_line:
        raise Exception("Expected to see the High Line in this tile, "
                        "but didn't.")
