# -*- coding: utf_8 -*-
"""Output formats."""
import json

from njsscan.logger import init_logger

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
            buffer.append(formatted)
            severity = details['metadata']['severity'].lower()
            if not outfile:
                if severity == 'error':
                    logger.error(formatted)
                elif severity == 'warning':
                    logger.warning(formatted)
                else:
                    logger.info(formatted)
    if outfile and buffer:
        outdata = '\n'.join(buffer)
        with open(outfile, 'w') as of:
            of.write(outdata)
    return buffer


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
    return json_output(outfile, sonarqube_report)


def get_sonarqube_issue(njsscan_issue):
    sonarqube_severity_mapping = {
        'ERROR': 'CRITICAL',
        'WARNING': 'MAJOR',
        'INFO': 'MINOR',
    }
    secondary_locations = []
    issue_data = njsscan_issue['metadata']
    # Handle missing controls
    if not njsscan_issue.get('files'):
        primary_location = None
    else:
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
