# -*- coding: utf_8 -*-
"""Tests for GitLab SAST report formatter."""
import json

from njsscan import __version__
from njsscan.formatters.gitlab_sast import (
    SCHEMA_VERSION,
    gitlab_sast_output,
    gitlab_severity,
)


def test_gitlab_severity_mapping():
    assert gitlab_severity('ERROR') == 'Critical'
    assert gitlab_severity('WARNING') == 'Medium'
    assert gitlab_severity('INFO') == 'Info'


def test_gitlab_sast_report_shape(tmp_path):
    scan_results = {
        'nodejs': {
            'express_xss': {
                'metadata': {
                    'description': (
                        'Untrusted User Input in Response will result '
                        'in Reflected Cross Site Scripting Vulnerability.'),
                    'severity': 'ERROR',
                    'cwe': (
                        'CWE-79: Improper Neutralization of Input During '
                        "Web Page Generation ('Cross-site Scripting')"),
                    'owasp-web': 'A1: Injection',
                    'reference': 'https://example.com/xss',
                },
                'files': [{
                    'file_path': 'app/routes.js',
                    'match_lines': [12, 14],
                    'match_position': [1, 20],
                    'match_string': 'res.send(req.query.q)',
                }],
            },
        },
        'templates': {
            'squirrelly_template': {
                'metadata': {
                    'description': (
                        'The Squirrelly.js template has an '
                        'unescaped variable.'),
                    'severity': 'WARNING',
                    'cwe': 'cwe-79',
                    'owasp-web': 'A1: Injection',
                },
                'files': [{
                    'file_path': 'views/page.html',
                    'match_lines': [10, 10],
                    'match_position': [5, 40],
                    'match_string': '{{ name | safe }}',
                }],
            },
        },
    }
    outfile = tmp_path / 'gl-sast-report.json'
    gitlab_sast_output(str(outfile), scan_results, __version__)
    report = json.loads(outfile.read_text())

    assert report['version'] == SCHEMA_VERSION
    assert report['scan']['type'] == 'sast'
    assert report['scan']['scanner']['id'] == 'njsscan'
    assert report['scan']['scanner']['version'] == __version__
    assert len(report['vulnerabilities']) == 2

    by_file = {v['location']['file']: v for v in report['vulnerabilities']}
    xss = by_file['app/routes.js']
    assert xss['severity'] == 'Critical'
    assert 'Cross Site Scripting' in xss['name']
    assert xss['location']['start_line'] == 12
    assert xss['location']['end_line'] == 14
    types = {i['type'] for i in xss['identifiers']}
    assert 'njsscan_rule_id' in types
    assert 'cwe' in types
    assert 'owasp' in types
    assert xss['links'][0]['url'] == 'https://example.com/xss'

    sqrl = by_file['views/page.html']
    assert sqrl['severity'] == 'Medium'
    assert sqrl['identifiers'][0]['value'] == 'squirrelly_template'


def test_gitlab_sast_missing_control_location(tmp_path):
    scan_results = {
        'nodejs': {
            'helmet_header_xss_filter': {
                'metadata': {
                    'description': 'Helmet XSS filter is not configured.',
                    'severity': 'INFO',
                    'cwe': 'cwe-693',
                },
            },
        },
        'templates': {},
    }
    outfile = tmp_path / 'gl-sast-report.json'
    gitlab_sast_output(str(outfile), scan_results, __version__)
    report = json.loads(outfile.read_text())
    vuln = report['vulnerabilities'][0]
    assert vuln['location']['file'] == '.'
    assert vuln['location']['start_line'] == 1
