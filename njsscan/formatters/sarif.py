# -*- coding: utf_8 -*-
"""SARIF output formatter for NodeJS scan results.

Based on https://github.com/microsoft/
bandit-sarif-formatter/blob/master/
bandit_sarif_formatter/formatter.py
MIT License, Copyright (c) Microsoft Corporation.

"""
from datetime import datetime, timezone
from pathlib import PurePath
import urllib.parse as urlparse

import sarif_om as om

from jschema_to_python.to_json import to_json

TS_FORMAT = '%Y-%m-%dT%H:%M:%SZ'


def level_from_severity(severity):
    return {
        'ERROR': 'error',
        'WARNING': 'warning',
        'INFO': 'note',
    }.get(severity, 'none')


def to_uri(file_path):
    pure_path = PurePath(file_path)
    if pure_path.is_absolute():
        return pure_path.as_uri()
    else:
        return urlparse.quote(pure_path.as_posix())


def format_rule_name(rule_id):
    return ''.join(word.capitalize() for word in rule_id.split('_'))


def add_results(scan_results, run):
    if run.results is None:
        run.results = []
    combined_results = {
        **scan_results.get('nodejs', {}),
        **scan_results.get('templates', {})}
    rules = {}
    rule_indices = {}

    for rule_id, issue_dict in combined_results.items():
        if 'files' not in issue_dict:
            continue
        result = create_rule_results(
            rule_id,
            issue_dict,
            rules,
            rule_indices)
        run.results.append(result)

    if rules:
        run.tool.driver.rules = list(rules.values())


def create_rule_results(rule_id, issue_dict, rules, rule_indices):
    rule_results = []

    rule, rule_index = rules.get(rule_id), rule_indices.get(rule_id)

    if not rule:
        doc = ('https://ajinabraham.'
               f'github.io/nodejsscan/#{rule_id}')
        cwe_id = issue_dict['metadata']['cwe'].split(':')[0].lower()
        rule = om.ReportingDescriptor(
            id=rule_id,
            name=format_rule_name(rule_id),
            help_uri=doc,
            properties={'tags': ['security', f'external/cwe/{cwe_id}']})
        rule_index = len(rules)
        rules[rule_id] = rule
        rule_indices[rule_id] = rule_index

    for item in issue_dict.get('files', []):
        location = create_location(item)
        rule_results.append(create_result(rule, rule_index, issue_dict, [location]))

    return rule_results


def create_location(item):
    return om.Location(
        physical_location=om.PhysicalLocation(
            artifact_location=om.ArtifactLocation(uri=to_uri(item['file_path'])),
            region=om.Region(
                start_line=item['match_lines'][0],
                end_line=item['match_lines'][1],
                start_column=item['match_position'][0],
                end_column=item['match_position'][1],
                snippet=om.ArtifactContent(text=item['match_string']))))


def create_result(rule, rule_index, issue_dict, locations):
    return om.Result(
        rule_id=rule.id,
        rule_index=rule_index,
        message=om.Message(text=issue_dict['metadata']['description']),
        level=level_from_severity(issue_dict['metadata']['severity']),
        locations=locations,
        properties={
            'owasp-web': issue_dict['metadata']['owasp-web'],
            'cwe': issue_dict['metadata']['cwe']})


def sarif_output(outfile, scan_results, njsscan_version):
    log = om.SarifLog(
        schema_uri=('https://raw.githubusercontent.com/'
                    'oasis-tcs/sarif-spec/master/Schemata/'
                    'sarif-schema-2.1.0.json'),
        version='2.1.0',
        runs=[om.Run(
            tool=om.Tool(driver=om.ToolComponent(
                name='nodejsscan',
                information_uri='https://github.com/ajinabraham/njsscan',
                semantic_version=njsscan_version,
                version=njsscan_version,
            )),
            invocations=[om.Invocation(
                end_time_utc=datetime.now(timezone.utc).strftime(TS_FORMAT),
                execution_successful=True,
            )])])
    run = log.runs[0]
    add_results(scan_results, run)
    json_out = to_json(log)

    if outfile:
        with open(outfile, 'w') as of:
            of.write(json_out)
    else:
        print(json_out)

    return json_out
