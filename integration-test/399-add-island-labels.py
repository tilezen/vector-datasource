# Natural Earth 110m
test.assert_has_feature(
    1, 0, 0, 'earth',
    { 'kind': 'earth', 'source': 'naturalearthdata.com' })

# Natural Earth 50m
test.assert_has_feature(
    2, 0, 1, 'earth',
    { 'kind': 'earth', 'source': 'naturalearthdata.com' })

# Natural Earth 10m
test.assert_has_feature(
    8, 40, 98, 'earth',
    { 'kind': 'earth', 'source': 'naturalearthdata.com' })

# OSM derived data from openstreetmapdata.com
test.assert_has_feature(
    9, 81, 197, 'earth',
    { 'kind': 'earth', 'source': 'openstreetmapdata.com' })



# NODE continent labels (from places)
# http://www.openstreetmap.org/node/36966063
test.assert_has_feature(
    1, 0, 0, 'earth',
    { 'kind': 'continent', 'label_placement': True, 'name': 'North America' })



# NODE archipelago labels (from place nodes)
# http://www.openstreetmap.org/node/3860848374
test.assert_has_feature(
    15, 10817, 11412, 'earth',
    { 'kind': 'archipelago', 'label_placement': True, 'min_zoom': 15,
      'name': 'Rochers aux Oiseaux' })

# LARGE archipelago labels (from place polygons)
# There aren't any today
# Really these should be lines, but will initially be points

# MEDIUM archipelago labels (from place polygons)
# Really these should be lines, but will initially be points
# http://www.openstreetmap.org/relation/6722301
test.assert_has_feature(
    15, 9367, 12534, 'earth',
    { 'kind': 'archipelago', 'label_placement': True, 'min_zoom': 15, 'name': 'Three Sisters Islands' })

# SMALL archipelago labels (from place polygons)
# Really these should be lines, but will initially be points
# http://www.openstreetmap.org/way/395338481
# In Europe, with a name, is exported
test.assert_has_feature(
    15, 18647, 9497, 'earth',
    { 'kind': 'archipelago', 'label_placement': True, 'name': 'Louekrinpaadet' })



# NODE island labels (from place nodes)
# http://www.openstreetmap.org/node/358796350
# Yerba Buena Island, near SF
test.assert_has_feature(
    15, 5245, 12661, 'earth',
    { 'kind': 'island', 'label_placement': True, 'name': 'Yerba Buena Island' })

# NODE island labels (from place nodes)
# http://www.openstreetmap.org/node/358761955
# Bird Island, north of SF
test.assert_has_feature(
    15, 5230, 12659, 'earth',
    { 'kind': 'island', 'label_placement': True, 'name': 'Bird Island' })

# NODE island labels (from place nodes)
# http://www.openstreetmap.org/node/358768646
# Kent Island, north of SF
test.assert_has_feature(
    15, 5217, 12649, 'earth',
    { 'kind': 'island', 'label_placement': True, 'name': 'Kent Island' })

# LARGE island labels (from place polygons)
# http://www.openstreetmap.org/relation/4227580
# Manitoulin Island, Canada
test.assert_has_feature(
    7, 34, 45, 'earth',
    { 'kind': 'island', 'label_placement': True, 'name': 'Manitoulin Island' })

# LARGE island labels (from place polygons)
# http://www.openstreetmap.org/relation/5176042
# Trinidad, the island of the nation
test.assert_has_feature(
    7, 42, 60, 'earth',
    { 'kind': 'island', 'label_placement': True, 'name': 'Trinidad' })

# MEDIUM island labels (from place polygons)
# http://www.openstreetmap.org/way/124916662
# Cockburn Island, Canada
test.assert_has_feature(
    9, 137, 182, 'earth',
    { 'kind': 'island', 'label_placement': True, 'name': 'Cockburn Island' })

# MEDIUM island labels (from place polygons)
# http://www.openstreetmap.org/relation/7117158
# San Miguel Island, California
test.assert_has_feature(
    10, 169, 408, 'earth',
    { 'kind': 'island', 'label_placement': True, 'name': 'San Miguel Island' })

# MEDIUM island labels (from place polygons)
# http://www.openstreetmap.org/way/40500922
# West Anacapa Island, California
test.assert_has_feature(
    12, 689, 1636, 'earth',
    { 'kind': 'island', 'label_placement': True, 'name': 'West Anacapa Island' })

# MEDIUM island labels (from place polygons)
# http://www.openstreetmap.org/way/157429145
# Angel Island, near SF
# 12, 654, 1581
test.assert_has_feature(
    12, 655, 1581, 'earth',
    { 'kind': 'island', 'label_placement': True, 'name': 'Angel Island' })

# SMALL island labels (from place polygons)
# http://www.openstreetmap.org/way/22693068
# Great Gull Island, NY state
test.assert_has_feature(
    15, 9819, 12261, 'earth',
    { 'kind': 'island', 'label_placement': True, 'name': 'Great Gull Island' })

# SMALL island labels (from place polygons)
# http://www.openstreetmap.org/way/308262375
# Goose Island, NY state
test.assert_has_feature(
    16, 19659, 24507, 'earth',
    { 'kind': 'island', 'label_placement': True, 'name': 'Goose Island' })

# SMALL island labels (from place polygons)
# http://www.openstreetmap.org/way/37248735
# Rincon Island, California
test.assert_has_feature(
    16, 11023, 26103, 'earth',
    { 'kind': 'island', 'label_placement': True, 'name': 'Rincon Island' })



# NODE islet labels (from place nodes)
# http://www.openstreetmap.org/node/358795646
# Pyramid Rock, SF
test.assert_has_feature(
    16, 10466, 25327, 'earth',
    { 'kind': 'islet', 'label_placement': True, 'name': 'Pyramid Rock', 'min_zoom': 17 })

# LARGE islet labels (from place polygons)
# http://www.openstreetmap.org/way/40500803
# Sugarloaf Island, west of SF
# 15, 5188, 12673
test.assert_has_feature(
    15, 5188, 12673, 'earth',
    { 'kind': 'islet', 'label_placement': True, 'name': 'Sugarloaf Island' })

# LARGE islet labels (from place polygons)
# http://www.openstreetmap.org/way/24433344
# Alcatraz Island, near SF
test.assert_has_feature(
    15, 5240, 12659, 'earth',
    { 'kind': 'islet', 'label_placement': True, 'name': 'Alcatraz Island' })

# MEDIUM islet labels (from place polygons)
# http://www.openstreetmap.org/way/157449982
# Bird Island, west of SF
test.assert_has_feature(
    16, 10493, 25303, 'earth',
    { 'kind': 'islet', 'label_placement': True, 'name': 'Bird Island' })

# SMALL islet labels (from place polygons)
# http://www.openstreetmap.org/way/306344403
# Sail Rock, near SF
test.assert_has_feature(
    16, 10467, 25395, 'earth',
    { 'kind': 'islet', 'label_placement': True, 'name': 'Sail Rock', 'min_zoom': 17 })

# SMALL islet labels (from place polygons)
# http://www.openstreetmap.org/way/32289183
# Little Mile Rock, SF
test.assert_has_feature(
    16, 10465, 25326, 'earth',
    { 'kind': 'islet', 'label_placement': True, 'name': 'Little Mile Rock', 'min_zoom': 17 })

# LARGE island labels (from place polygons)
# http://www.openstreetmap.org/relation/4227580
# Manitoulin Island, Canada
test.assert_has_feature(
    7, 34, 45, 'earth',
    { 'kind': 'island', 'label_placement': True, 'name': 'Manitoulin Island' })

# LARGE island labels (from place polygons)
# http://www.openstreetmap.org/relation/5176042
# Trinidad, the island of the nation
test.assert_has_feature(
    7, 42, 60, 'earth',
    { 'kind': 'island', 'label_placement': True, 'name': 'Trinidad' })

# island polygon split across multiple tiles shouldn't get a label placement
# in each tile, only one.
# http://www.openstreetmap.org/way/26767313
# Treasure Island, San Francisco
test.assert_has_feature(
    14, 2622, 6329, 'earth',
    { 'kind': 'island', 'label_placement': True, 'name': 'Treasure Island' })
# neighbouring tiles should not have a placement
test.assert_no_matching_feature(
    14, 2623, 6329, 'earth',
    { 'kind': 'island', 'label_placement': True, 'name': 'Treasure Island' })
test.assert_no_matching_feature(
    14, 2622, 6340, 'earth',
    { 'kind': 'island', 'label_placement': True, 'name': 'Treasure Island' })
test.assert_no_matching_feature(
    14, 2623, 6340, 'earth',
    { 'kind': 'island', 'label_placement': True, 'name': 'Treasure Island' })

# multi-polygonal islands
# http://www.openstreetmap.org/relation/5344925
# Islas Marietas
# main island should get label
test.assert_has_feature(
    15, 6773, 14457, 'earth',
    { 'kind': 'island', 'label_placement': True, 'name': 'Islas Marietas' })
# FUTURE: smaller island parts should not
#test.assert_no_matching_feature(
#    15, 6774, 14457, 'earth',
#    { 'kind': 'island', 'label_placement': True, 'name': 'Islas Marietas' })
#test.assert_no_matching_feature(
#    15, 6775, 14457, 'earth',
#    { 'kind': 'island', 'label_placement': True, 'name': 'Islas Marietas' })
