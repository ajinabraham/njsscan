# -*- coding: utf_8 -*-
"""Defect Dojo output format."""

import re
from njsscan.formatters.json_out import json_output
from datetime import datetime

cvss_impact_mapping = {
        "INFO": {"C": "N", "I": "N", "A": "N"},
        "WARNING": {"C": "L", "I": "L", "A": "N"},
        "ERROR": {"C": "H", "I": "H", "A": "H"},
    }

# Function to extract CWE number
def extract_cwe_number(cwe_string):
    match = re.search(r"\d+", cwe_string)
    return match.group(0) if match else ""

# Function to generate CVSSv3 string
def generate_cvssv3_string(severity, attack_vector="N", attack_complexity="L", privileges_required="N", user_interaction="N", scope="U"):
    impacts = cvss_impact_mapping.get(severity.upper(), {"C": "N", "I": "N", "A": "N"})
    return f"CVSS:3.1/AV:{attack_vector}/AC:{attack_complexity}/PR:{privileges_required}/UI:{user_interaction}/S:{scope}/C:{impacts['C']}/I:{impacts['I']}/A:{impacts['A']}"

def get_defectdojo_issue(value):
    severity_mapping = {
        "INFO": "Info",
        "WARNING": "High",
        "ERROR": "Critical"
    }

    base_description = value.get("metadata", {}).get("description", "")
    owasp_web = value.get("metadata", {}).get("owasp-web", "")
    match_strings = [file_data.get("match_string", "") for file_data in value.get("files", [])]
    concatenated_description = f"{base_description}\n\nOWASP Reference: {owasp_web}\n\nMatched Strings:\n" + "\n".join(match_strings)

    # Map severity
    raw_severity = value.get("metadata", {}).get("severity", "High")
    severity = severity_mapping.get(raw_severity.upper(), "High")

    # Extract CWE number
    raw_cwe = value.get("metadata", {}).get("cwe", "")
    cwe = extract_cwe_number(raw_cwe)

    endpoints = [file_data.get("file_path", "") for file_data in value.get("files", [])]
    file_path = value.get("files", [{}])[0].get("file_path", "") if value.get("files") else ""
    line = value.get("files", [{}])[0].get("match_lines", [None])[0]

    # Generate CVSSv3 string
    cvssv3_string = generate_cvssv3_string(
        severity=raw_severity,
        attack_vector="N",  # Network
        attack_complexity="L",  # Low
        privileges_required="N",  # None
        user_interaction="N",  # None
        scope="U"  # Unchanged
    )

    issue = {
        "description": concatenated_description,
        "severity": severity,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "cwe": cwe,
        "file_path": file_path,
        "line": line,
        "endpoints": endpoints,
        "cvssv3": cvssv3_string
    }

    return issue


def defectdojo_output(outfile, scan_results, version):
    """Defect Dojo JSON Output."""
    defectdojo_issues = []
    for i in ['nodejs', 'templates']:
        for k, v in scan_results[i].items():
            # print(v)
            issue = get_defectdojo_issue(v)
            issue['title'] = k.replace("_", " ").title()
            defectdojo_issues.append(issue)
    defectdojo_report = {
        'findings': defectdojo_issues,
    }
    return json_output(outfile, defectdojo_report, version)
