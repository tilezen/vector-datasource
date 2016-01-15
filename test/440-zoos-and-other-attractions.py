# expect these features in _both_ the landuse and POIs layers.
for layer in ['pois', 'landuse']:

    # So the question here is if kind should be set to attraction or enclosure.
    # There are other attraction areas (like rides at amusement parks), so I
    # vote of emphasizing the value of zoo in the enclosure case (where zoo=*
    # has been defined).
    #
    # kind: enclosure, attraction: animal, name: Asian Rhino, natural: sand and
    # tourism: attraction
    # assert_has_feature(
    #     19, 83737, 202725, layer,
    #     { 'id': -5695997,
    #       'osm_relation': True,
    #       'kind': 'enclosure',
    #       'attraction': 'animal',
    #       'name': 'Asian Rhino',
    #       'natural': 'sand',
    #       'tourism': 'attraction' })

    # In the case of this Hong Kong amusement park ride, a more specific key set
    # beyond tourism: attraction hasn't been set, so I'd expect kind:
    # attraction.
    # NOTE: updated to a feature in North America: MarineLand, Niagara Falls,
    # ON.
    assert_has_feature(
        17, 36746, 48133, layer,
        { 'id': 177402901,
          'kind': 'attraction' })

    # pipe through religion on resorts
    # La Foret Conference & Retreat Center (way 228716140)
    assert_has_feature(
        15, 6852, 12522, layer,
        { 'kind': 'resort',
          'religion': 'christian' })

# NOTE: because these are also buildings, they don't appear in the
# landuse layer.
# See https://github.com/mapzen/vector-datasource/issues/201

# But in the case of this Disneyland ride, there's been an attraction:
# carousel set in addition to tourism: attraction so I expect the kind:
# carousel to be set.
#
# TAGS: attraction=carousel, building=yes, name=King Arthur Carrousel,
# tourism=attraction
assert_has_feature(
    19, 90412, 209763, 'pois',
    { 'id': 129691054,
      'kind': 'carousel' })

# Same for this kind: roller_coaster.
# TAGS: attraction=roller_coaster, building=yes, name=Matterhorn Bobsleds,
# tourism=attraction
## way 107280556 http://c.tile.openstreetmap.org/17/22603/52441.png
assert_has_feature(
    17, 22603, 52441, 'pois',
    { 'id': 107280556,
      'kind': 'roller_coaster' })
