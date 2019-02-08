from vectordatasource.meta.kinds import parse_all_kinds


if __name__ == '__main__':
    from vectordatasource.meta import find_yaml_path
    import argparse
    import os.path

    yaml_path = find_yaml_path()
    sort_rank_path = os.path.join(
        os.path.split(yaml_path)[0], 'spreadsheets', 'sort_rank')
    parser = argparse.ArgumentParser()
    parser.add_argument('--yaml-path', help='Directory containing YAML',
                        default=yaml_path)
    parser.add_argument('--sort-rank-path', help='Directory containing sort '
                        'rank CSVs.', default=sort_rank_path)
    parser.add_argument('--kind-detail', help='Include kind_detail.',
                        action='store_true', default=False)
    args = parser.parse_args()

    if args.yaml_path:
        yaml_path = args.yaml_path

    if args.sort_rank_path:
        sort_rank_path = args.sort_rank_path

    all_kinds = parse_all_kinds(yaml_path, sort_rank_path, args.kind_detail)

    row_fmt = "%(layer)12s %(kind)30s %(min_zoom)8s %(sort_rank)s"
    if args.kind_detail:
        row_fmt = "%(layer)12s %(kind)30s %(kind_detail)30s " \
                  "%(min_zoom)8s %(sort_rank)s"

    print row_fmt % dict(layer="LAYER", kind="KIND", kind_detail="KIND_DETAIL",
                         min_zoom="MIN_ZOOM", sort_rank="SORT_RANK")
    for k in sorted(all_kinds):
        v = all_kinds[k]
        print row_fmt % \
            dict(layer=k.layer, kind=k.kind, kind_detail=k.kind_detail,
                 min_zoom=repr(v.min_zoom), sort_rank=repr(v.sort_rank))
