# -*- coding: utf_8 -*-
"""JSON output format."""
import json


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
