# if we're merging, then only one of these will be in tiles. if both exist
# then it's more likely that no merging is happening.
#
# http://www.openstreetmap.org/way/89912879
# http://www.openstreetmap.org/way/89911760
assert_has_feature(
    16, 19829, 24234, "roads",
    {"kind": "major_road", "highway": "trunk", "id": 89912879})
assert_has_feature(
    16, 19829, 24234, "roads",
    {"kind": "major_road", "highway": "trunk", "id": 89911760})
