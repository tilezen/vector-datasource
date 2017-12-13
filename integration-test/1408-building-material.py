from . import FixtureTest


class BuildingMaterial(FixtureTest):

    def test_building_material(self):
        self.load_fixtures([
            'https://www.openstreetmap.org/way/135174116',
        ])

        self.assert_has_feature(
            16, 10484, 25327, 'buildings',
            {'id': 135174116, 'kind': 'building',
             'building_material': 'brick'})

    def test_building_part_material(self):
        self.load_fixtures([
            'https://www.openstreetmap.org/way/451331532',
        ])

        self.assert_has_feature(
            16, 10484, 25324, 'buildings',
            {'id': 451331532, 'kind': 'building_part',
             'building_material': 'concrete'})
