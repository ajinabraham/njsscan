# -*- coding: utf_8 -*-
"""DefectDojo Generic Findings Import JSON output format."""
import hashlib
import re
from datetime import date

from njsscan.formatters.json_out import json_output

SEVERITY_MAPPING = {
    'ERROR': 'High',
    'WARNING': 'Medium',
    'INFO': 'Info',
}


def extract_cwe(cwe_value):
    """Return CWE id as int, or None if unavailable."""
    if isinstance(cwe_value, int):
        return cwe_value
    if not cwe_value:
        return None
    match = re.search(r'\d+', str(cwe_value))
    if not match:
        return None
    return int(match.group(0))


def build_description(meta, match_string=None):
    """Build finding description from rule metadata and optional match."""
    parts = [meta.get('description', '').strip()]
    owasp = meta.get('owasp-web')
    if owasp:
        parts.append(f'OWASP: {owasp}')
    if match_string:
        parts.append(f'Match:\n{match_string}')
    return '\n\n'.join(part for part in parts if part)


def unique_id(rule_id, file_path, line):
    """Stable id for DefectDojo reimport/dedup."""
    raw = f'{rule_id}|{file_path or ""}|{line if line is not None else ""}'
    return hashlib.sha256(raw.encode('utf-8')).hexdigest()[:32]


def get_defectdojo_findings(rule_id, issue):
    """Convert one njsscan rule result into DefectDojo finding dicts."""
    meta = issue.get('metadata', {})
    severity = SEVERITY_MAPPING.get(
        meta.get('severity', 'WARNING').upper(),
        'Medium',
    )
    cwe = extract_cwe(meta.get('cwe'))
    references = meta.get('owasp-web') or meta.get('cwe') or ''
    files = issue.get('files') or [None]
    findings = []

    for file_data in files:
        file_path = None
        line = None
        match_string = None
        if file_data:
            file_path = file_data.get('file_path')
            match_lines = file_data.get('match_lines') or []
            if match_lines:
                line = int(match_lines[0])
            match_string = file_data.get('match_string')

        finding = {
            'title': rule_id.replace('_', ' ').title(),
            'severity': severity,
            'description': build_description(meta, match_string),
            'date': date.today().isoformat(),
            'active': True,
            'verified': False,
            'false_p': False,
            'out_of_scope': False,
            'static_finding': True,
            'dynamic_finding': False,
            'vuln_id_from_tool': rule_id,
            'unique_id_from_tool': unique_id(rule_id, file_path, line),
            'tags': ['njsscan'],
        }
        if cwe is not None:
            finding['cwe'] = cwe
        if references:
            finding['references'] = str(references)
        if file_path:
            finding['file_path'] = file_path
        if line is not None:
            finding['line'] = line
        findings.append(finding)
    return findings


def defectdojo_output(outfile, scan_results, version):
    """Emit DefectDojo Generic Findings Import JSON."""
    findings = []
    for section in ('nodejs', 'templates'):
        for rule_id, issue in scan_results.get(section, {}).items():
            findings.extend(get_defectdojo_findings(rule_id, issue))

    report = {
        'name': 'njsscan',
        'type': 'njsscan',
        'version': version,
        'findings': findings,
    }
    return json_output(outfile, report, version)
