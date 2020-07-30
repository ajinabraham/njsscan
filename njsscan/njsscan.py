# -*- coding: utf_8 -*-
"""The nodejsscan cli: njsscan."""
from libsast import Scanner

from njsscan import settings
from njsscan.utils import (
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
            'sgrep_extensions': conf['nodejs_extensions'],
            'match_extensions': conf['template_extensions'],
            'ignore_filenames': conf['ignore_filenames'],
            'ignore_extensions': conf['ignore_extensions'],
            'ignore_paths': conf['ignore_paths'],
            'ignore_rules': conf['ignore_rules'],
            'show_progress': not json,
        }
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
        self.post_ignore_rules()
        self.post_ignore_files()

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

    def post_ignore_rules(self):
        """Ignore findings by rules."""
        for rule_id in self.options['ignore_rules']:
            if rule_id in self.result['nodejs']:
                del self.result['nodejs'][rule_id]
            if rule_id in self.result['templates']:
                del self.result['templates'][rule_id]

    def post_ignore_files(self):
        """Ignore file by rule."""
        del_keys = set()
        for rule_id, details in self.result['nodejs'].items():
            files = details.get('files')
            if not files:
                continue
            for file in files:
                mstr = file.get('match_string')
                if 'ignore:' in mstr and rule_id in mstr:
                    details['files'].remove(file)
                if len(details['files']) == 0:
                    del_keys.add(rule_id)
        for rid in del_keys:
            if rid in self.result['nodejs']:
                del self.result['nodejs'][rid]
