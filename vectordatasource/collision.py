from vectordatasource.meta.python import FilterCompiler
from vectordatasource.meta.python import create_matcher


class CollisionRanker(object):

    def __init__(self, cases):
        def _output_fn(datum):
            return datum['index']

        index = 1
        matchers = []
        for case in cases:
            assert isinstance(case, dict)

            # if it's a reserved block, check the syntax and assert that the
            # indices are reserved. note that reserved block indices are
            # inclusive of both the "from" and "to".
            if '_reserved' in case:
                # reserved should be the only key, to avoid confusion with
                # filter blocks.
                assert case.keys() == ['_reserved']

                reserved = case['_reserved']

                # we can reserve either a specific range of indices, or a
                # count.
                if reserved.keys() == ['count']:
                    # just increment the index to skip. we can't collide with
                    # anything, so there's no assertion to make.
                    index += reserved['count']

                else:
                    from_index = reserved['from']
                    to_index = reserved['to']

                    # check that we've not used this index already.
                    assert index <= from_index, "Unable to satisfy reserved " \
                        "block: already at index %d, and wanted to reserve " \
                        "from %d." % (index, from_index)

                    # start counting again past the "to" reserved index.
                    index = to_index + 1

            else:
                matcher = create_matcher(
                    {'filter': case, 'index': index}, _output_fn)
                matchers.append(matcher)
                index += 1

        filter_compiler = FilterCompiler()
        ast_fn, compiled_fn = filter_compiler.compile(
            matchers, 'collision_rank')

        self.fn = compiled_fn

    def __call__(self, feature):
        shape, props, fid = feature
        meta = None
        return self.fn(shape, props, fid, meta)
