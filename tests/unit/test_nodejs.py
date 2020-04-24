"""Test Node.js rules."""
from .setup_test import (
    get_paths,
    scanner,
)


EXPECTED = [
    'njsscan.rules.semantic_grep.node_aes_ecb',
    'njsscan.rules.semantic_grep.node_sha1',
    'njsscan.rules.semantic_grep.node_md5',
    'njsscan.rules.semantic_grep.node_ssrf',
    'njsscan.rules.semantic_grep.express_xss',
    'njsscan.rules.semantic_grep.eval_nodejs',
    'njsscan.rules.semantic_grep.express_cors_2',
    'njsscan.rules.semantic_grep.header_xss_generic',
    'njsscan.rules.semantic_grep.generic_path_traversal3_warning',
    'njsscan.rules.semantic_grep.generic_path_traversal2',
    'njsscan.rules.semantic_grep.eval_warning',
    'njsscan.rules.semantic_grep.express_open_redirect',
    'njsscan.rules.semantic_grep.generic_header_injection',
    'njsscan.rules.semantic_grep.express_cors',
    'njsscan.rules.semantic_grep.node_deserialize',
    'njsscan.rules.semantic_grep.yaml_deserialize2',
    'njsscan.rules.semantic_grep.yaml_deserialize',
    'njsscan.rules.semantic_grep.generic_os_command_exec',
    'njsscan.rules.semantic_grep.express_bodyparser',
    'njsscan.rules.semantic_grep.generic_cors',
    'njsscan.rules.semantic_grep.header_xss_lusca',
    'njsscan.rules.semantic_grep.header_xss_generic_2',
    'njsscan.rules.semantic_grep.node_password',
    'njsscan.rules.semantic_grep.node_api_key',
    'njsscan.rules.semantic_grep.node_tls_reject',
    'njsscan.rules.semantic_grep.node_curl_ssl_verify_disable',
    'njsscan.rules.semantic_grep.handlebars_safestring',
    'njsscan.rules.semantic_grep.handlebars_noescape',
]


def test_nodejs():
    paths = get_paths()
    truepos = paths['true_positives']
    res = scanner([truepos])
    assert len(res['nodejs'].keys()) != 0


def test_nodejs_rules():
    paths = get_paths()
    truepos = paths['true_positives']
    trueneg = paths['true_negatives']
    pos_files = list(truepos.glob('**/*.js'))
    neg_files = list(trueneg.glob('**/*.js'))
    assert len(pos_files) == len(neg_files)
    res = scanner(pos_files)
    actual = [*res['nodejs']]
    assert actual == EXPECTED
    res = scanner(neg_files)
    assert res['nodejs'] == {}
