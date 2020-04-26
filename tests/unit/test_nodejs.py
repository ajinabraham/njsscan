"""Test Node.js rules."""
from .setup_test import (
    get_paths,
    scanner,
)


EXPECTED = [
    'rule.semantic_grep.eval_nodejs',
    'rule.semantic_grep.eval_warning',
    'rule.semantic_grep.express_bodyparser',
    'rule.semantic_grep.express_cors',
    'rule.semantic_grep.express_cors2',
    'rule.semantic_grep.express_open_redirect',
    'rule.semantic_grep.express_xss',
    'rule.semantic_grep.generic_cors',
    'rule.semantic_grep.generic_header_injection',
    'rule.semantic_grep.generic_os_command_exec',
    'rule.semantic_grep.generic_path_traversal2',
    'rule.semantic_grep.generic_path_traversal3_warning',
    'rule.semantic_grep.handlebars_noescape',
    'rule.semantic_grep.handlebars_safestring',
    'rule.semantic_grep.hardcoded_jwt_secret',
    'rule.semantic_grep.header_xss_generic',
    'rule.semantic_grep.header_xss_generic2',
    'rule.semantic_grep.header_xss_lusca',
    'rule.semantic_grep.helmet_feature_disabled',
    'rule.semantic_grep.helmet_header_check_crossdomain',
    'rule.semantic_grep.helmet_header_check_csp',
    'rule.semantic_grep.helmet_header_check_expect_ct',
    'rule.semantic_grep.helmet_header_dns_prefetch',
    'rule.semantic_grep.helmet_header_feature_policy',
    'rule.semantic_grep.helmet_header_frame_guard',
    'rule.semantic_grep.helmet_header_hsts',
    'rule.semantic_grep.helmet_header_ienoopen',
    'rule.semantic_grep.helmet_header_nosniff',
    'rule.semantic_grep.helmet_header_referrer_policy',
    'rule.semantic_grep.helmet_header_x_powered_by',
    'rule.semantic_grep.helmet_header_xss_filter',
    'rule.semantic_grep.node_jwt_none_algorithm',
    'rule.semantic_grep.node_aes_ecb',
    'rule.semantic_grep.node_api_key',
    'rule.semantic_grep.node_curl_ssl_verify_disable',
    'rule.semantic_grep.node_deserialize',
    'rule.semantic_grep.node_insecure_random_generator',
    'rule.semantic_grep.node_md5',
    'rule.semantic_grep.node_password',
    'rule.semantic_grep.node_secret',
    'rule.semantic_grep.node_sha1',
    'rule.semantic_grep.node_ssrf',
    'rule.semantic_grep.node_timing_attack',
    'rule.semantic_grep.node_tls_reject',
    'rule.semantic_grep.yaml_deserialize',
    'rule.semantic_grep.yaml_deserialize2',
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
    actual.sort()
    EXPECTED.sort()
    assert actual == EXPECTED
    res = scanner(neg_files)
    assert res['nodejs'] == {}
