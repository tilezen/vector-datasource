# global:
#   # NOTE: Natural Earth 1:50 million used zooms 0,1,2,3,4
#   #       and only has USA, Canada, Brazil, and Australia
#   #       all with scalerank of 2 (a documented NE omission).
#   #       Then 1:10 million NE is selected at zooms 5, 6, 7
#   #       and includes most all countries, with various scalerank
#   #       but is inconsistent with 1:50 in scalerank=2 so countries
#   #       like Russia will "pop" in at 5, but with min_zoom of 2
#   #       (and India, China, Indonesia, and South Africa).
#   - &ne_region_boundaries_min_zoom |
#       CASE WHEN scalerank =   0 THEN  6.7
#            WHEN scalerank <=  2 THEN  2
#            WHEN scalerank <=  3 THEN  3
#            WHEN scalerank <=  4 THEN  5
#            WHEN scalerank <=  5 THEN  5.5
#            WHEN scalerank <=  6 THEN  6
#            WHEN scalerank <=  7 THEN  6.7
#            WHEN scalerank <=  8 THEN  6.8
#            WHEN scalerank <=  9 THEN  7
#       END


# ne data


# map_unit min_zoom

# England-Wales boundary in United Kingdom (scalerank=4, 1:10m NE only)
test.assert_has_feature(
    5, 15, 10, 'boundaries',
    { 'kind': 'map_unit', 'min_zoom': 5, 'sort_rank': 258})


# region min_zoom (via scalerank)

# USA region (scalerank=2, 1:50m NE and 1:10m NE)
test.assert_has_feature(
    2, 0, 1, 'boundaries',
    { 'kind': 'region', 'min_zoom': 2})

# Germany region (scalerank=3, 1:10m NE only)
test.assert_has_feature(
    5, 17, 10, 'boundaries',
    { 'kind': 'region', 'min_zoom': 3})

# Mexico region (scalerank=4, 1:10m NE only)
test.assert_has_feature(
    5, 7, 14, 'boundaries',
    { 'kind': 'region', 'min_zoom': 5})

# Poland region (scalerank=5, 1:10m NE only)
test.assert_has_feature(
    5, 17, 10, 'boundaries',
    { 'kind': 'region', 'min_zoom': 5.5})

# Austria region (scalerank=6, 1:10m NE only)
test.assert_has_feature(
    6, 34, 22, 'boundaries',
    { 'kind': 'region', 'min_zoom': 6})

# Sweden region (scalerank=7, 1:10m NE only)
test.assert_has_feature(
    6, 35, 18, 'boundaries',
    { 'kind': 'region', 'min_zoom': 6.7})

# United Kingdom region (scalerank=8, 1:10m NE only)
test.assert_has_feature(
    6, 31, 18, 'boundaries',
    { 'kind': 'region', 'min_zoom': 6.8})

# Switzerland region (scalerank=9, 1:10m NE only)
test.assert_has_feature(
    7, 66, 44, 'boundaries',
    { 'kind': 'region', 'min_zoom': 7})


# dropping of name

# USA region NO name, Natural Earth
test.assert_has_feature(
    2, 0, 1, 'boundaries',
    { 'kind': 'region', 'name': type(None)})

# Germany region NO name, Natural Earth
test.assert_has_feature(
    5, 17, 10, 'boundaries',
    { 'kind': 'region', 'name': type(None)})

# Mexico region NO name, Natural Earth
test.assert_has_feature(
    5, 7, 14, 'boundaries',
    { 'kind': 'region', 'name': type(None)})

# Poland region NO name, Natural Earth
test.assert_has_feature(
    5, 17, 10, 'boundaries',
    { 'kind': 'region', 'name': type(None)})

# Austria region NO name, Natural Earth
test.assert_has_feature(
    6, 34, 22, 'boundaries',
    { 'kind': 'region', 'name': type(None)})

# Austria region HAS name, Natural Earth
test.assert_has_feature(
    7, 68, 44, 'boundaries',
    { 'kind': 'region', 'name': 'Tirol - Salzburg'})


# Switzerland region HAS name, OpenStreetMap
# http://www.openstreetmap.org/relation/1686447
# http://www.openstreetmap.org/relation/1685677
test.assert_has_feature(
    8, 133, 89, 'boundaries',
    { 'kind': 'region', 'name': 'Zug - Luzern'})

# Austria region HAS name, OpenStreetMap
# http://www.openstreetmap.org/relation/52343
# http://www.openstreetmap.org/relation/86539
test.assert_has_feature(
    8, 136, 89, 'boundaries',
    { 'kind': 'region', 'name': 'Salzburg - Tirol' })
