"""Test Template rules."""
from .setup_test import (
    get_paths,
    scanner,
)


RULE_IDS = [
    'rule.underscore_template',
    'rule.pug_jade_template',
    'rule.ejs_ect_template',
    'rule.vue_template',
    'rule.handlebar_mustache_template',
    'rule.dust_template',
]


def test_templates():
    paths = get_paths()
    tmpl_files = paths['template_files']
    res = scanner([tmpl_files])
    assert len(res['templates'].keys()) != 0


def test_templates_rules():
    paths = get_paths()
    tmpl_files = paths['template_files']
    res = scanner([tmpl_files])
    actual = [*res['templates']]
    actual.sort()
    RULE_IDS.sort()
    assert actual == RULE_IDS
