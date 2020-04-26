"""Test Template rules."""
from .setup_test import (
    get_paths,
    scanner,
)


EXPECTED = [
    'rule.underscore_template',
    'rule.pug_jade_template',
    'rule.ejs_ect_template',
    'rule.vue_template',
    'rule.handlebar_mustache_template',
    'rule.dust_template',
]


def test_templates():
    paths = get_paths('templates')
    tmpl_files = paths['template_dir']
    res = scanner([tmpl_files])
    assert len(res['templates'].keys()) != 0


def test_templates_rules():
    paths = get_paths('templates')
    truepos = paths['true_positives']
    trueneg = paths['true_negatives']
    pos_files = list(truepos.glob('**/*'))
    neg_files = list(trueneg.glob('**/*'))
    assert len(pos_files) == len(neg_files)
    res = scanner(pos_files)
    actual = [*res['templates']]
    actual.sort()
    EXPECTED.sort()
    assert actual == EXPECTED
    res = scanner(neg_files)
    assert res['templates'] == {}