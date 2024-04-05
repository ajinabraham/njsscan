#!/usr/bin/env python
# -*- coding: utf_8 -*-
"""The nodejsscan cli: njsscan."""
import argparse
import sys

from njsscan import __version__
from njsscan.njsscan import NJSScan
from njsscan.formatters import (
    cli,
    json_out,
    sarif,
    sonarqube,
)


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
    parser.add_argument('--sarif',
                        help='set output format as SARIF 2.1.0',
                        action='store_true')
    parser.add_argument('--sonarqube',
                        help='set output format compatible with SonarQube',
                        action='store_true')
    parser.add_argument('--html',
                        help='set output format as HTML',
                        action='store_true')
    parser.add_argument('-o', '--output',
                        help='output filename to save the result',
                        required=False)
    parser.add_argument('-c', '--config',
                        help='Location to .njsscan config file',
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
        is_json = args.json or args.sonarqube or args.sarif
        scan_results = NJSScan(
            args.path,
            is_json,
            args.missing_controls,
            args.config,
        ).scan()
        if args.sonarqube:
            sonarqube.sonarqube_output(
                args.output,
                scan_results,
                __version__)
        elif args.json:
            json_out.json_output(
                args.output,
                scan_results,
                __version__)
        elif args.sarif:
            sarif.sarif_output(
                args.output,
                scan_results,
                __version__)
        elif args.html:
            cli.cli_output(
                args.output,
                scan_results,
                __version__,
                'unsafehtml')
        else:
            cli.cli_output(
                args.output,
                scan_results,
                __version__,
                'fancy_grid')
        handle_exit(scan_results, args.exit_warning)

    elif args.version:
        cli.print_tool_info(__version__)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
