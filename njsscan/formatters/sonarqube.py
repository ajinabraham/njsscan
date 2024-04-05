# -*- coding: utf_8 -*-
"""Sonarqube output format."""

from njsscan.formatters.json_out import json_output


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
                'endColumn': file['match_position'][1] - 1,
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


def sonarqube_output(outfile, scan_results, version):
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
    return json_output(outfile, sonarqube_report, version)
