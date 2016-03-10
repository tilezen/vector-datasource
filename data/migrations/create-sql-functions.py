from collections import namedtuple
from jinja2 import Environment
from jinja2 import FileSystemLoader
from TileStache.Goodies.VecTiles.transform import _parse_kt
import csv

Rule = namedtuple('Rule', 'min_zoom_calc equals not_exists set_memberships')


def create_rule(keys, row, min_zoom_calc):
    equals = []
    not_exists = []
    set_memberships = []
    for key, matcher in zip(keys, row):
        assert matcher, 'Invalid value for row: %s' % row
        # skip all * values
        if matcher == '*':
            continue
        if matcher == '-':
            not_exists.append(key)
        elif ';' in matcher:
            candidates = matcher.split(';')
            set_memberships.append((key, candidates))
        else:
            equals.append((key, matcher))
    assert equals or not_exists, 'Invalid rule: %s' % row
    return Rule(min_zoom_calc, equals, not_exists, set_memberships)


def format_key(key):
    if key.startswith('tags->'):
        key = 'tags->\'%s\'' % (key[len('tags->'):])
    else:
        key = '"%s"' % key
    return key


def create_case_statement(rules):
    when_parts = []
    for rule in rules:
        when_equals = ''
        when_not_exists = ''
        when_in = ''

        when_conds = []

        if rule.equals:
            when_equals_parts = ['%s = \'%s\'' % (format_key(key), matcher)
                                 for key, matcher in rule.equals]
            when_equals = ' AND '.join(when_equals_parts)
            when_conds.append(when_equals)

        if rule.not_exists:
            when_not_exists_parts = ['%s IS NULL' % format_key(key)
                                     for key in rule.not_exists]
            when_not_exists = ' AND '.join(when_not_exists_parts)
            when_conds.append(when_not_exists)

        if rule.set_memberships:
            when_in_parts = ['%s IN (%s)' % (format_key(key),
                                             ', '.join(candidates))
                             for key, candidates in rule.set_memberships]
            when_in = ' AND '.join(when_in_parts)
            when_conds.append(when_in)

        when_cond = ' AND '.join(when_conds)
        when_part = 'WHEN %s THEN %s' % (when_cond, rule.min_zoom_calc)
        when_parts.append(when_part)

    case_statement = 'CASE\n%s\nEND' % '\n'.join(when_parts)
    return case_statement


rules = []
with open('../../spreadsheets/kind/landuse.csv') as fh:
    reader = csv.reader(fh, skipinitialspace=True)
    keys = None
    for row in reader:
        if keys is None:
            # assume the last key is the kind value
            row.pop(-1)
            # assume the second to last key is the min_zoom
            # TODO this might need to be changed once we have more files in play
            min_zoom = row.pop(-1)
            assert min_zoom == 'min_zoom'
            keys = []
            for key_type in row:
                key, typ = _parse_kt(key_type)
                keys.append(key)
        else:
            # assume kind is last
            _ = row.pop(-1)
            # and next is the min_zoom calculation
            min_zoom_calc = row.pop(-1)
            # is this variable syntax necessary?
            # we can assume that the string will just be valid sql
            # TODO remove the variable syntax
            assert (min_zoom_calc.startswith('${') and
                    min_zoom_calc.endswith('}')), 'Unexpected min_zoom'
            min_zoom_calc = min_zoom_calc[2:-1]
            rule = create_rule(keys, row, min_zoom_calc)
            rules.append(rule)

case_statement = create_case_statement(rules)
template_name = 'sql.jinja2'
environment = Environment(loader=FileSystemLoader('.'))
template = environment.get_template(template_name)
sql = template.render(case_statement=case_statement)
print sql
