# -*- coding: utf_8 -*-
"""The nodejsscan cli: njsscan."""
from libsast import Scanner

from njsscan import settings
from njsscan.utils import (
    find_sgrep_bin,
    get_config,
    read_missing_controls,
)


class NJSScan:
    def __init__(self, paths, json, check_controls) -> None:
        conf = get_config(paths)
        self.check_controls = check_controls
        self.options = {
            'match_rules': settings.PATTERN_RULES_DIR,
            'sgrep_rules': settings.SGREP_RULES_DIR,
            'sgrep_binary': find_sgrep_bin(),
            'sgrep_extensions': conf['nodejs_extensions'],
            'match_extensions': conf['template_extensions'],
            'ignore_filenames': conf['ignore_filenames'],
            'ignore_extensions': conf['ignore_extensions'],
            'ignore_paths': conf['ignore_paths'],
        }
        if not json:
            self.options['show_progress'] = True
        self.paths = paths
        self.result = {
            'templates': {},
            'nodejs': {},
            'errors': [],
        }

    def scan(self) -> dict:
        """Start Scan."""
        scanner = Scanner(self.options, self.paths)
        result = scanner.scan()
        if result:
            self.format_output(result)
        return self.result

    def format_output(self, results) -> dict:
        """Format to njsscan friendly output."""
        self.format_sgrep(results['semantic_grep'])
        self.format_matches(results['pattern_matcher'])

    def missing_controls(self, result):
        """Check for missing controls."""
        controls = read_missing_controls()['controls']
        result_keys = result['nodejs'].keys()
        for rule_id in settings.GOOD_CONTROLS_ID:
            if rule_id in result_keys:
                # Good! Control is present
                del result['nodejs'][rule_id]
            else:
                if self.check_controls:
                    result['nodejs'][rule_id] = controls[rule_id]
                else:
                    continue

    def format_sgrep(self, sgrep_output):
        """Remove metavars from sgrep output."""
        self.result['errors'] = sgrep_output['errors']
        for rule_id in sgrep_output['matches']:
            for finding in sgrep_output['matches'][rule_id]['files']:
                finding.pop('metavars', None)
        self.result['nodejs'] = sgrep_output['matches']
        self.missing_controls(self.result)

    def format_matches(self, matcher_out):
        """Format Pattern Matcher output."""
        self.result['templates'] = matcher_out
