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

NODEJS_FILE_EXTENSIONS = {
    '.js',
    '',
}
TEMPLATE_FILE_EXTENSIONS = {
    '.html', '.mustache', '.hbs', '.vue',
    '.hdbs', '.ejs', '.dust', '.json',
    '.tl', '.tpl', '.tmpl', '.pug',
    '.ect', '.sh', '.yml', '.toml', '.jade',
}
IGNORE_FILENAMES = {
    '.DS_Store', 'jquery.min.js', 'axios.min.js',
    'bootstrap-tour.js', 'raphael-min.js', 'react.js',
    'tinymce.min.js', 'tinymce.js', 'vue.min.js',
    'codemirror-compressed.js', 'codemirror.js',
    'react.production.min.js', 'react-dom.production.min.js',
    'bootstrap.min.js', 'd3.min.js', 'angular.min.js',
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
}
