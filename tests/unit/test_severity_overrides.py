# -*- coding: utf_8 -*-
"""Tests for .njsscan severity-overrides."""
from njsscan.njsscan import NJSScan
from njsscan.utils import (
    get_config,
    normalize_severity_overrides,
)


def test_normalize_severity_overrides():
    assert normalize_severity_overrides(None) == {}
    assert normalize_severity_overrides(['express_xss']) == {}
    assert normalize_severity_overrides({
        'express_xss': 'error',
        'squirrelly_template': ' WARNING ',
        'bad': 'critical',
        '': 'ERROR',
    }) == {
        'express_xss': 'ERROR',
        'squirrelly_template': 'WARNING',
    }


def test_get_config_reads_severity_overrides(tmp_path):
    cfg = tmp_path / '.njsscan'
    cfg.write_text(
        '---\n'
        '- severity-overrides:\n'
        '    express_xss: ERROR\n'
        '    squirrelly_template: warning\n',
        encoding='utf-8')
    options = get_config([str(tmp_path)], False)
    assert options['severity_overrides'] == {
        'express_xss': 'ERROR',
        'squirrelly_template': 'WARNING',
    }


def test_post_override_severities_before_filter(tmp_path):
    cfg = tmp_path / 'custom.njsscan'
    cfg.write_text(
        '---\n'
        '- severity-overrides:\n'
        '    express_xss: ERROR\n'
        '  severity-filter:\n'
        '  - ERROR\n',
        encoding='utf-8')
    scan = NJSScan([str(tmp_path)], True, False, config=str(cfg))
    scan.result = {
        'nodejs': {
            'express_xss': {
                'metadata': {
                    'description': 'xss',
                    'severity': 'INFO',
                },
            },
            'other_rule': {
                'metadata': {
                    'description': 'x',
                    'severity': 'WARNING',
                },
            },
        },
        'templates': {
            'squirrelly_template': {
                'metadata': {
                    'description': 'tmpl',
                    'severity': 'WARNING',
                },
            },
        },
        'errors': [],
    }
    scan.post_override_severities()
    assert scan.result['nodejs']['express_xss']['metadata']['severity'] == (
        'ERROR')
    scan.post_ignore_rules_by_severity('nodejs')
    scan.post_ignore_rules_by_severity('templates')
    assert 'express_xss' in scan.result['nodejs']
    assert 'other_rule' not in scan.result['nodejs']
    assert 'squirrelly_template' not in scan.result['templates']


def test_severity_override_ignored_for_missing_rule(tmp_path):
    cfg = tmp_path / '.njsscan'
    cfg.write_text(
        '---\n'
        '- severity-overrides:\n'
        '    missing_rule: ERROR\n',
        encoding='utf-8')
    scan = NJSScan([str(tmp_path)], True, False, config=str(cfg))
    scan.result = {
        'nodejs': {
            'express_xss': {
                'metadata': {'severity': 'INFO'},
            },
        },
        'templates': {},
        'errors': [],
    }
    scan.post_override_severities()
    assert scan.result['nodejs']['express_xss']['metadata']['severity'] == (
        'INFO')
