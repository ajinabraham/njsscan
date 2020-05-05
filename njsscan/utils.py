# -*- coding: utf_8 -*-
"""Logger Config."""
from pathlib import Path

import njsscan.settings as config
from njsscan.logger import init_logger

import yaml


logger = init_logger(__name__)

# TODO write yaml validatpr


def get_config(base_path):
    options = {
        'nodejs_extensions': config.NODEJS_FILE_EXTENSIONS,
        'template_extensions': config.TEMPLATE_FILE_EXTENSIONS,
        'ignore_filenames': config.IGNORE_FILENAMES,
        'ignore_extensions': config.IGNORE_EXTENSIONS,
        'ignore_paths': config.IGNORE_PATHS,
    }
    cfile = Path(base_path[0]) / config.NJSSCAN_CONFIG_FILE
    if cfile.is_file() and cfile.exists():
        extras = read_yaml(cfile)
        if not extras:
            return options
        root = extras[0]
        usr_njs_ext = root.get('nodejs-extensions')
        usr_tmpl_ext = root.get('template-extensions')
        usr_ignore_files = root.get('ignore-filenames')
        usr_igonre_paths = root.get('ignore-paths')
        usr_ignore_exts = root.get('ignore-extensions')
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
    return options


def read_missing_controls():
    """Read missing controls yaml."""
    return read_yaml(config.MISSING_CONTROLS)


def find_sgrep_bin():
    """Find Semantic Grep Binary."""
    return None


def read_yaml(file_obj, text=False):
    try:
        if text:
            return yaml.safe_load(file_obj)
        return yaml.safe_load(file_obj.read_text('utf-8', 'ignore'))
    except yaml.YAMLError:
        logger.error('Failed to parse YAML')
    except Exception:
        logger.exception('Error parsing YAML')
    return None
