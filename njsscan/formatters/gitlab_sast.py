# -*- coding: utf_8 -*-
"""GitLab SAST report formatter.

Produces JSON conforming to GitLab's SAST report schema so findings can be
uploaded with artifacts:reports:sast (no SARIF converter required).

See: https://docs.gitlab.com/development/integrations/secure/
Schema: https://gitlab.com/gitlab-org/security-products/security-report-schemas
"""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import PurePath
import json
import re

from njsscan.formatters.sarif import format_rule_name

# Widely supported GitLab security-report schema version
SCHEMA_VERSION = '15.0.4'
TS_FORMAT = '%Y-%m-%dT%H:%M:%S'
SCANNER_URL = 'https://github.com/ajinabraham/njsscan'
_CWE_ID_RE = re.compile(r'(?i)cwe-?(\d+)')
_MAX_NAME = 255


def gitlab_severity(severity):
    """Map njsscan severity to GitLab SAST severity."""
    return {
        'ERROR': 'Critical',
        'WARNING': 'Medium',
        'INFO': 'Info',
    }.get((severity or '').upper(), 'Unknown')


def gitlab_confidence(severity):
    """Map njsscan severity to GitLab confidence."""
    return {
        'ERROR': 'High',
        'WARNING': 'High',
        'INFO': 'Medium',
    }.get((severity or '').upper(), 'Unknown')


def _vuln_id(rule_id, file_path, start_line, end_line):
    raw = f'{rule_id}|{file_path}|{start_line}|{end_line}'
    return sha256(raw.encode('utf-8')).hexdigest()


def _relative_file(file_path):
    if not file_path:
        return '.'
    return PurePath(file_path).as_posix()


def _cwe_id(cwe):
    """Return normalized CWE-NNN id from metadata, if present."""
    if not cwe:
        return None
    match = _CWE_ID_RE.search(str(cwe).split(':', 1)[0])
    if not match:
        return None
    return f'CWE-{match.group(1)}'


def _first_sentence(text):
    """Return a short title from the first sentence of description."""
    if not text:
        return ''
    cleaned = ' '.join(str(text).strip().split())
    for sep in ('. ', '? ', '! '):
        if sep in cleaned:
            cleaned = cleaned.split(sep, 1)[0]
            break
    else:
        cleaned = cleaned.rstrip('.?!')
    return cleaned.strip()


def vulnerability_name(rule_id, metadata):
    """Build a human-readable vulnerability name for GitLab."""
    title = _first_sentence(metadata.get('description'))
    if not title:
        title = format_rule_name(rule_id)
    cwe_id = _cwe_id(metadata.get('cwe'))
    if cwe_id and cwe_id not in title.upper():
        title = f'{title} ({cwe_id})'
    if len(title) > _MAX_NAME:
        title = title[:_MAX_NAME - 1].rstrip() + '…'
    return title


def _cwe_identifier(cwe):
    cwe_id = _cwe_id(cwe)
    if not cwe_id:
        return None
    num = cwe_id.split('-', 1)[1]
    return {
        'type': 'cwe',
        'name': cwe_id,
        'value': num,
        'url': f'https://cwe.mitre.org/data/definitions/{num}.html',
    }


def _named_identifier(id_type, value, name=None, url=None):
    if not value:
        return None
    text = str(value).strip()
    if not text:
        return None
    ident = {
        'type': id_type,
        'name': name or text,
        'value': text.split(':', 1)[0].strip(),
    }
    if url:
        ident['url'] = url
    return ident


def build_identifiers(rule_id, metadata):
    """Build GitLab identifiers from rule id and njsscan metadata."""
    identifiers = [{
        'type': 'njsscan_rule_id',
        'name': f'njsscan-{rule_id}',
        'value': rule_id,
    }]
    cwe = _cwe_identifier(metadata.get('cwe'))
    if cwe:
        identifiers.append(cwe)
    owasp = _named_identifier(
        'owasp',
        metadata.get('owasp-web'),
        name=metadata.get('owasp-web'))
    if owasp:
        identifiers.append(owasp)
    return identifiers


def build_links(metadata):
    ref = metadata.get('reference') or metadata.get('ref')
    if not ref:
        return []
    return [{'url': ref}]


def create_vulnerability(rule_id, issue_dict, file_item=None):
    """Create one GitLab SAST vulnerability object."""
    meta = issue_dict.get('metadata') or {}
    description = meta.get('description') or rule_id
    name = vulnerability_name(rule_id, meta)

    if file_item:
        file_path = _relative_file(file_item.get('file_path'))
        start_line = int(file_item.get('match_lines', [1, 1])[0] or 1)
        end_line = int(file_item.get('match_lines', [1, 1])[1] or start_line)
    else:
        file_path = '.'
        start_line = 1
        end_line = 1

    vuln = {
        'id': _vuln_id(rule_id, file_path, start_line, end_line),
        'category': 'sast',
        'name': name,
        'message': name,
        'description': description,
        'severity': gitlab_severity(meta.get('severity')),
        'confidence': gitlab_confidence(meta.get('severity')),
        'scanner': {
            'id': 'njsscan',
            'name': 'njsscan',
        },
        'location': {
            'file': file_path,
            'start_line': start_line,
            'end_line': end_line,
        },
        'identifiers': build_identifiers(rule_id, meta),
    }
    links = build_links(meta)
    if links:
        vuln['links'] = links
    return vuln


def build_vulnerabilities(scan_results):
    """Collect vulnerabilities from nodejs and templates results."""
    vulnerabilities = []
    combined = {
        **(scan_results.get('nodejs') or {}),
        **(scan_results.get('templates') or {}),
    }
    for rule_id, issue in combined.items():
        files = issue.get('files') or []
        if not files:
            vulnerabilities.append(create_vulnerability(rule_id, issue))
            continue
        for file_item in files:
            vulnerabilities.append(
                create_vulnerability(rule_id, issue, file_item))
    return vulnerabilities


def build_scan(version, start_time, end_time, status='success'):
    """Build the GitLab scan metadata block."""
    scanner = {
        'id': 'njsscan',
        'name': 'njsscan',
        'url': SCANNER_URL,
        'vendor': {'name': 'OpenSecurity'},
        'version': version,
    }
    return {
        'analyzer': dict(scanner),
        'scanner': scanner,
        'type': 'sast',
        'start_time': start_time,
        'end_time': end_time,
        'status': status,
    }


def gitlab_sast_output(outfile, scan_results, version):
    """Write or print a GitLab SAST report."""
    now = datetime.now(timezone.utc).strftime(TS_FORMAT)
    report = {
        'version': SCHEMA_VERSION,
        'vulnerabilities': build_vulnerabilities(scan_results),
        'scan': build_scan(version, now, now),
    }
    jout = json.dumps(
        report,
        sort_keys=True,
        indent=2,
        separators=(',', ': '))
    if outfile:
        with open(outfile, 'w') as of:
            of.write(jout)
    else:
        print(jout)
    return jout
