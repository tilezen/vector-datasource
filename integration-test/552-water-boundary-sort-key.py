# from https://github.com/mapzen/vector-datasource/issues/552
test.assert_has_feature(
    16, 10487, 25327, "water",
    {"kind": "ocean", "boundary": True, "sort_rank": 205})
