#!/usr/bin/env python
# -*- coding: utf_8 -*-
"""The nodejsscan cli: njsscan."""
import argparse
import json
import sys

from njsscan import __version__
from njsscan.logger import init_logger
from njsscan.njsscan import NJSScan

logger = init_logger(__name__)


def cli_out(rule_id, details):
    """Get CLI friendly format."""
    items = []
    items.append('\n==================================================='
                 '===================================================')
    items.append(f'RULE ID: {rule_id}')
    for meta, value in details['metadata'].items():
        if meta == 'id':
            continue
        meta_format = meta.upper().replace('_', '')
        items.append(f'{meta_format}: {value}')
    items.append('==================================================='
                 '===================================================')
    files = details.get('files')
    if not files:
        return '\n'.join(items)
    items.append('\n__________________FILES___________________________')
    for match in files:
        items.append('\n')
        file_path = match['file_path']
        items.append(f'File: {file_path}')
        position = match['match_position']
        items.append(f'Match Position: {position[0]} - {position[1]}')
        lines = match.get('match_lines')
        line = (lines[0] if lines[0] == lines[1]
                else f'{lines[0]}: {lines[1]}')
        items.append(f'Line Number(s): {line}')
        match_string = match['match_string']
        if isinstance(match_string, list):
            match_string = '\n'.join(ln.strip() for ln in match_string)
        items.append(f'Match String: {match_string}')
    return '\n'.join(items)


def format_output(outfile, scan_results):
    """Format output printing."""
    if not scan_results:
        return
    scan_results.pop('errors', None)
    buffer = []
    for out in scan_results:
        for rule_id, details in scan_results[out].items():
            formatted = cli_out(rule_id, details)
            if outfile:
                buffer.append(formatted)
            else:
                if details['metadata']['severity'].lower() == 'error':
                    logger.error(formatted)
                elif details['metadata']['severity'].lower() == 'warning':
                    logger.warning(formatted)
                else:
                    logger.info(formatted)
    if buffer:
        outdata = '\n'.join(buffer)
        with open(outfile, 'w') as of:
            of.write(outdata)


def json_output(outfile, scan_results):
    """JSON Output."""
    if outfile:
        with open(outfile, 'w') as of:
            json.dump(scan_results, of, sort_keys=True,
                      indent=2, separators=(',', ': '))
    else:
        json_output = (json.dumps(scan_results, sort_keys=True,
                                  indent=2, separators=(',', ': ')))
        print(json_output)
        return json_output


def sonarqube_output(outfile, scan_results):
    """Sonarqube JSON Output."""
    sonarqube_issues = []
    for i in ['nodejs', 'templates']:
        for k, v in scan_results[i].items():
            issue = get_sonarqube_issue(v)
            issue['ruleId'] = k
            sonarqube_issues.append(issue)
    sonarqube_report = {
        'issues': sonarqube_issues,
    }
    json_output(outfile, sonarqube_report)


def get_sonarqube_issue(njsscan_issue):
    sonarqube_severity_mapping = {
        'ERROR': 'CRITICAL',
        'WARNING': 'MAJOR',
        'INFO': 'MINOR',
    }
    secondary_locations = []
    issue_data = njsscan_issue['metadata']
    for ix, file in enumerate(njsscan_issue['files']):
        text_range = {
            'startLine': file['match_lines'][0],
            'endLine': file['match_lines'][1],
            'startColumn': file['match_position'][0],
            'endColumn': file['match_position'][1],
        }
        location = {
            'message': issue_data['description'],
            'filePath': file['file_path'],
            'textRange': text_range,
        }
        if ix == 0:
            primary_location = location
        else:
            secondary_locations.append(location)
    issue = {
        'engineId': 'njsscan',
        'type': 'VULNERABILITY',
        'severity': sonarqube_severity_mapping[issue_data['severity']],
        'primaryLocation': primary_location,
    }
    if secondary_locations:
        issue['secondaryLocations'] = secondary_locations
    return issue


def handle_exit(results, exit_warn):
    """Handle Exit."""
    combined = {}
    if results.get('nodejs'):
        combined.update(results['nodejs'])
    if results.get('templates'):
        combined.update(results['templates'])
    for meta in combined.values():
        severity = meta['metadata']['severity']
        ewarn = severity == 'WARNING' and exit_warn
        if severity == 'ERROR' or ewarn:
            sys.exit(1)
    sys.exit(0)


def main():
    """Main CLI."""
    parser = argparse.ArgumentParser()
    parser.add_argument('path',
                        nargs='*',
                        help=('Path can be file(s) or '
                              'directories with source code'))
    parser.add_argument('--json',
                        help='set output format as JSON',
                        action='store_true')
    parser.add_argument('--sonarqube',
                        help='set output format compatible with SonarQube',
                        action='store_true')
    parser.add_argument('-o', '--output',
                        help='output filename to save the result',
                        required=False)
    parser.add_argument('--missing-controls',
                        help='enable missing security controls check',
                        action='store_true',
                        required=False)
    parser.add_argument('-w', '--exit-warning',
                        help='non zero exit code on warning',
                        action='store_true',
                        required=False)
    parser.add_argument('-v', '--version',
                        help='show njsscan version',
                        required=False,
                        action='store_true')
    args = parser.parse_args()
    if args.path:
        is_json = args.json or args.sonarqube
        scan_results = NJSScan(
            args.path,
            is_json,
            args.missing_controls,
        ).scan()
        if args.sonarqube:
            sonarqube_output(args.output, scan_results)
        elif args.json:
            json_output(args.output, scan_results)
        else:
            format_output(args.output, scan_results)

        handle_exit(scan_results, args.exit_warning)

    elif args.version:
        print('njsscan: v' + __version__)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
