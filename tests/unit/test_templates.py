"""Test Template rules."""
from .setup_test import (
    get_paths,
    scanner,
)


EXPECTED = [
    'underscore_template',
    'pug_jade_template',
    'ejs_ect_template',
    'vue_template',
    'handlebar_mustache_template',
    'dust_template',
    'squirrelly_template',
    'electronjs_node_integration',
    'electronjs_disable_websecurity',
]


def test_templates():
    paths = get_paths('templates')
    tmpl_files = paths['template_dir']
    res = scanner([tmpl_files], False)
    assert len(res['templates'].keys()) != 0


def test_templates_rules():
    paths = get_paths('templates')
    truepos = paths['true_positives']
    trueneg = paths['true_negatives']
    pos_files = list(truepos.glob('**/*'))
    neg_files = list(trueneg.glob('**/*'))
    assert len(pos_files) == len(neg_files)
    res = scanner(pos_files, False)
    actual = [*res['templates']]
    actual.sort()
    EXPECTED.sort()
    assert actual == EXPECTED
    res = scanner(neg_files, False)
    assert res['templates'] == {}
