#!/usr/bin/env python
# -*- coding: utf_8 -*-
"""The nodejsscan cli: njsscan."""
import argparse
import json
import sys

from njsscan import __version__
from njsscan.njsscan import NJSScan


def handle_output(out, scan_results):
    """Output."""
    if out:
        # out is the fully qualified path and filename
        # for the ouptput file.
        # We recommend you use a .json extension
        with open(out, 'w') as outfile:
            json.dump(scan_results, outfile, sort_keys=True,
                      indent=4, separators=(',', ': '))
    else:
        print((json.dumps(scan_results, sort_keys=True,
                          indent=4, separators=(',', ': '))))


def handle_exit(results):
    # TODO FIX
    if results:
        sys.exit(1)
    sys.exit(0)


def main():
    """Main CLI."""
    parser = argparse.ArgumentParser()
    parser.add_argument('path',
                        nargs='*',
                        help=('Path can be file(s) or '
                              'directories with Node.js source code'))
    parser.add_argument('--no-strict',
                        help='Scan non Node.js files as well.',
                        action='store_true')
    parser.add_argument('-o', '--output',
                        help='Output filename to save JSON report.',
                        required=False)
    parser.add_argument('-v', '--version',
                        help='Show njsscan version',
                        required=False,
                        action='store_true')
    args = parser.parse_args()
    if args.path:
        scan_results = NJSScan(args).scan()
        handle_output(args.output, scan_results)
        handle_exit(scan_results)
    elif args.version:
        print('nodejsscan: njscli v' + __version__)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
