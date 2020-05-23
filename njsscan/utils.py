# -*- coding: utf_8 -*-
"""Logger Config."""
from pathlib import Path

import njsscan.settings as config
from njsscan.logger import init_logger

import yaml


logger = init_logger(__name__)


def get_config(base_path):
    options = {
        'nodejs_extensions': config.NODEJS_FILE_EXTENSIONS,
        'template_extensions': config.TEMPLATE_FILE_EXTENSIONS,
        'ignore_filenames': config.IGNORE_FILENAMES,
        'ignore_extensions': config.IGNORE_EXTENSIONS,
        'ignore_paths': config.IGNORE_PATHS,
        'ignore_rules': set(),
    }
    cfile = Path(base_path[0]) / config.NJSSCAN_CONFIG_FILE
    if cfile.is_file() and cfile.exists():
        extras = read_yaml(cfile)
        root = validate_config(extras, options)
        if not root:
            logger.warning('Invalid YAML, ignoring config from .njsscan')
            return options
        usr_njs_ext = root.get('nodejs-extensions')
        usr_tmpl_ext = root.get('template-extensions')
        usr_ignore_files = root.get('ignore-filenames')
        usr_igonre_paths = root.get('ignore-paths')
        usr_ignore_exts = root.get('ignore-extensions')
        usr_ignore_rules = root.get('ignore-rules')
        if usr_njs_ext:
            options['nodejs_extensions'].update(usr_njs_ext)
        if usr_tmpl_ext:
            options['template_extensions'].update(usr_tmpl_ext)
        if usr_ignore_files:
            options['ignore_filenames'].update(usr_ignore_files)
        if usr_igonre_paths:
            options['ignore_paths'].update(usr_igonre_paths)
        if usr_ignore_exts:
            options['ignore_extensions'].update(usr_ignore_exts)
        if usr_ignore_rules:
            options['ignore_rules'].update(usr_ignore_rules)
    return options


def validate_config(extras, options):
    """Validate user supplied config file."""
    if not extras:
        return False
    if isinstance(extras, dict):
        root = extras
    else:
        root = extras[0]
    valid = True
    for key, value in root.items():
        if key.replace('-', '_') not in options.keys():
            valid = False
            logger.warning('The config `%s` is not supported.', key)
        if not isinstance(value, list):
            valid = False
            logger.warning('The value `%s` for the config `%s` is invalid.'
                           ' Only list of value(s) are supported.', value, key)
    if not valid:
        return False
    return root


def read_missing_controls():
    """Read missing controls yaml."""
    return read_yaml(config.MISSING_CONTROLS)


def read_yaml(file_obj, text=False):
    """Read Yaml."""
    try:
        if text:
            return yaml.safe_load(file_obj)
        return yaml.safe_load(file_obj.read_text('utf-8', 'ignore'))
    except yaml.YAMLError:
        logger.error('Failed to parse YAML')
    except Exception:
        logger.exception('Error parsing YAML')
    return None
