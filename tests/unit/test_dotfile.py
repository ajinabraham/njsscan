"""Test njsscan dotfile."""
from .setup_test import (
    get_paths,
    scanner,
)


TMPL_IDS = [
    'underscore_template',
]

NJS_IDS = [
    'node_aes_ecb',
    'generic_path_traversal',
]


def test_njsscan_dotfile():
    paths = get_paths('nodejs')
    files = paths['dot_file']
    res = scanner([files], False)
    tmpl = [*res['templates']]
    njs = [*res['nodejs']]
    tmpl.sort()
    njs.sort()
    TMPL_IDS.sort()
    NJS_IDS.sort()
    assert tmpl == TMPL_IDS
    assert njs == NJS_IDS
