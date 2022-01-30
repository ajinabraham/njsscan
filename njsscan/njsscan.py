# -*- coding: utf_8 -*-
"""The nodejsscan cli: njsscan."""
from linecache import getline

from libsast import (
    Scanner,
    standards,
)

from njsscan import settings
from njsscan.utils import (
    get_config,
    read_missing_controls,
)


class NJSScan:
    def __init__(self, paths, json, check_controls, config=False) -> None:
        conf = get_config(paths, config)
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
            'severity_filter': conf['severity_filter'],
            'show_progress': not json,
        }
        self.paths = paths
        self.result = {
            'templates': {},
            'nodejs': {},
            'errors': [],
        }
        self.standards = standards.get_standards()

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
        self.post_ignore_rules_by_severity('nodejs')
        self.post_ignore_rules_by_severity('template')
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
                    self.expand_mappings(controls[rule_id])
                    result['nodejs'][rule_id] = controls[rule_id]
                else:
                    continue

    def expand_mappings(self, meta):
        """Expand libsast standard mappings."""
        meta_keys = meta['metadata'].keys()
        for mkey in meta_keys:
            if mkey not in self.standards.keys():
                continue
            to_expand = meta['metadata'][mkey]
            expanded = self.standards[mkey].get(to_expand)
            if expanded:
                meta['metadata'][mkey] = expanded

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

    def post_ignore_rules_by_severity(self, key):
        """Filter findings by rule severity."""
        del_keys = set()
        if key not in self.result:
            return
        for rule_id, details in self.result[key].items():
            issue_severity = details.get('metadata').get('severity')
            if issue_severity not in self.options['severity_filter']:
                del_keys.add(rule_id)
        for rid in del_keys:
            if rid in self.result[key]:
                del self.result[key][rid]

    def suppress_pm_comments(self, obj, rule_id):
        """Suppress pattern matcher."""
        file_path = obj['file_path']
        lines = obj['match_lines']
        match_line = getline(file_path, lines[0])
        if 'njsscan-ignore:' in match_line and rule_id in match_line:
            return True
        return False

    def post_ignore_files(self):
        """Ignore file by rule."""
        del_keys = set()
        for rule_id, details in self.result['nodejs'].items():
            files = details.get('files')
            if not files:
                continue
            tmp_files = files.copy()
            for file in files:
                mstr = file.get('match_string')
                if 'njsscan-ignore:' in mstr and rule_id in mstr:
                    tmp_files.remove(file)
                if len(tmp_files) == 0:
                    del_keys.add(rule_id)
            details['files'] = tmp_files
        for rule_id, details in self.result['templates'].items():
            files = details.get('files')
            if not files:
                continue
            tmp_files = files.copy()
            for file in files:
                mstr = file.get('match_string')
                if self.suppress_pm_comments(file, rule_id):
                    tmp_files.remove(file)
                if len(tmp_files) == 0:
                    del_keys.add(rule_id)
            details['files'] = tmp_files
        # Remove Rule IDs marked for deletion.
        for rid in del_keys:
            if rid in self.result['nodejs']:
                del self.result['nodejs'][rid]
            if rid in self.result['templates']:
                del self.result['templates'][rid]
