# -*- coding: utf_8 -*-
"""JSON output format."""
import json


def json_output(outfile, scan_results, version):
    """JSON Output."""
    scan_results['njsscan_version'] = version
    json_output = json.dumps(
        scan_results,
        sort_keys=True,
        indent=2,
        separators=(',', ': '))
    if outfile:
        with open(outfile, 'w') as of:
            of.write(json_output)
    else:
        print(json_output)
    return json_output
