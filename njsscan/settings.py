#!/usr/bin/env python
# -*- coding: utf_8 -*-
"""Settings."""
from pathlib import Path

NJSSCAN_CONFIG_FILE = '.njsscan'
BASE_DIR = Path(__file__).resolve().parent
SGREP_RULES_DIR = (
    BASE_DIR / 'rules' / 'semantic_grep'
).as_posix()
PATTERN_RULES_DIR = (
    BASE_DIR / 'rules' / 'pattern_matcher'
).as_posix()
MISSING_CONTROLS = (
    BASE_DIR / 'rules' / 'missing_controls.yaml'
)

NODEJS_FILE_EXTENSIONS = {
    '.js',
    '',
}
TEMPLATE_FILE_EXTENSIONS = {
    '.html', '.mustache', '.hbs', '.vue',
    '.hdbs', '.ejs', '.dust', '.json',
    '.tl', '.tpl', '.tmpl', '.pug', '.haml',
    '.ect', '.sh', '.yml', '.toml', '.jade',
}
IGNORE_FILENAMES = {
    '.DS_Store', 'jquery.js', 'axios.js',
    'bootstrap-tour.js', 'raphael-min.js', 'react.js',
    'tinymce.js', 'vue.js', 'codemirror-compressed.js',
    'codemirror.js', 'bootstrap.js', 'angular.js',
    'react-dom.production.js', 'react.production.js',
}
IGNORE_EXTENSIONS = {
    '.zip', '.7z', '.tz',
    '.rar', '.exe', '.o', '.a',
}
IGNORE_PATHS = {
    '__MACOSX',
    'node_modules',
    'bower_components',
    'fixtures',
    'jquery',
    'spec',
    'example',
    '.min.js',
    '.git',
    '.svn',
}
GOOD_CONTROLS_ID = {
    'anti_csrf_control',
    'rate_limit_control',
    'helmet_header_check_csp',
    'helmet_header_check_expect_ct',
    'helmet_header_feature_policy',
    'helmet_header_frame_guard',
    'helmet_header_dns_prefetch',
    'helmet_header_x_powered_by',
    'helmet_header_hsts',
    'helmet_header_ienoopen',
    'helmet_header_nosniff',
    'helmet_header_referrer_policy',
    'helmet_header_xss_filter',
    'helmet_header_check_crossdomain',
}

SEVERITY_FILTER = (
    'INFO',
    'WARNING',
    'ERROR',
)
