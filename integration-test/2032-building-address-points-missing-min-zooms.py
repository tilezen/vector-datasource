# -*- encoding: utf-8 -*-
import dsl

from . import FixtureTest


class BuildingAddressPointsMissingMinZooms(FixtureTest):

    def test_address_point_gen_has_min_zoom_17(self):
        import dsl

        z, x, y = (17, 19299, 24630)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/265302092
            dsl.way(265302092, dsl.tile_box(z, x, y), {
                'addr:city': 'New York',
                'addr:housenumber': '1071',
                'addr:postcode': '10018',
                'addr:street': '6th Avenue',
                'building': 'yes',
                'building:colour': '#86816E',
                'building:levels': '12',
                'height': '46.6',
                'name': '1071 Sixth Avenue',
                'nycdoitt:bin': '1022566',
                'roof:material': 'concrete',
                'roof:shape': 'flat',
                'source': 'openstreetmap.org',
                'start_date': '1920',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'buildings', {
                'id': 265302092,
                'addr_housenumber': '1071',
                'kind': 'address',
                'min_zoom': 17
            })

    # at zoom 15, there should be no address points generated
    def test_no_address_points_generated_below_zoom_16(self):
        import dsl

        z, x, y = (15, 9649, 12315)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/265302092
            dsl.way(265302092, dsl.tile_box(z, x, y), {
                'addr:city': 'New York',
                'addr:housenumber': '1071',
                'addr:postcode': '10018',
                'addr:street': '6th Avenue',
                'building': 'yes',
                'building:colour': '#86816E',
                'building:levels': '12',
                'height': '46.6',
                'name': '1071 Sixth Avenue',
                'nycdoitt:bin': '1022566',
                'roof:material': 'concrete',
                'roof:shape': 'flat',
                'source': 'openstreetmap.org',
                'start_date': '1920',
            }),
        )

        self.assert_no_matching_feature(
            z, x, y, 'buildings', {
                'kind': 'address',
            })

    # if there is no housenumber, and the building name is just a number, use that
    def test_address_point_falls_back_to_name(self):
        import dsl

        z, x, y = (17, 19299, 24630)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/265302092
            dsl.way(265302092, dsl.tile_box(z, x, y), {
                'addr:city': 'New York',
                # omitted 'addr:housenumber': '1071',
                'addr:postcode': '10018',
                'addr:street': '6th Avenue',
                'building': 'yes',
                'building:colour': '#86816E',
                'building:levels': '12',
                'height': '46.6',
                'name': '999',  # modified to be a number
                'nycdoitt:bin': '1022566',
                'roof:material': 'concrete',
                'roof:shape': 'flat',
                'source': 'openstreetmap.org',
                'start_date': '1920',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'buildings', {
                'id': 265302092,
                'addr_housenumber': '999',
                'kind': 'address',
                'min_zoom': 17
            })

    # if there is no housenumber, and the building name is not just a number, don't make an address point
    def test_no_address_point_if_no_usable_address(self):
        import dsl

        z, x, y = (16, 19299, 24630)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/265302092
            dsl.way(265302092, dsl.tile_box(z, x, y), {
                'addr:city': 'New York',
                # omitted 'addr:housenumber': '1071',
                'addr:postcode': '10018',
                'addr:street': '6th Avenue',
                'building': 'yes',
                'building:colour': '#86816E',
                'building:levels': '12',
                'height': '46.6',
                'name': '1071 Sixth Avenue',
                'nycdoitt:bin': '1022566',
                'roof:material': 'concrete',
                'roof:shape': 'flat',
                'source': 'openstreetmap.org',
                'start_date': '1920',
            }),
        )

        self.assert_no_matching_feature(
            z, x, y, 'buildings', {
                'kind': 'address',
            })
