from unittest import TestCase


class YamlRulesTest(TestCase):

    def test_all_kinds(self):
        """
        Test that we've enumerated all the possible values for kind and
        kind_detail in the YAML files.
        """

        from vectordatasource.meta import find_yaml_path
        from vectordatasource.meta.kinds import parse_all_kinds
        import os.path

        yaml_path = find_yaml_path()
        sort_rank_path = os.path.join(
            os.path.split(yaml_path)[0], 'spreadsheets', 'sort_rank')

        # should be able to execute this without throwing an exception.
        all_kinds = parse_all_kinds(yaml_path, sort_rank_path, True)

        # and we should get some data back
        self.assertTrue(all_kinds)
