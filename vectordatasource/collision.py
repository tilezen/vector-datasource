from vectordatasource.meta.python import FilterCompiler
from vectordatasource.meta.python import create_matcher


class CollisionRanker(object):

    def __init__(self, cases):
        def _output_fn(datum):
            return datum['index']

        index = 1
        matchers = []
        for case in cases:
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
