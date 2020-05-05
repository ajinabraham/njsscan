"""Test Node.js rules."""
from .setup_test import (
    get_paths,
    scanner,
)


EXPECTED = [
    'eval_nodejs',
    'eval_warning',
    'express_bodyparser',
    'express_cors',
    'express_cors2',
    'express_open_redirect',
    'express_xss',
    'generic_cors',
    'generic_header_injection',
    'generic_os_command_exec',
    'generic_path_traversal2',
    'generic_path_traversal3_warning',
    'handlebars_noescape',
    'handlebars_safestring',
    'hardcoded_jwt_secret',
    'header_xss_generic',
    'header_xss_generic2',
    'header_xss_lusca',
    'helmet_feature_disabled',
    'node_jwt_none_algorithm',
    'node_aes_ecb',
    'node_api_key',
    'node_curl_ssl_verify_disable',
    'node_deserialize',
    'node_entity_expansion',
    'node_insecure_random_generator',
    'node_md5',
    'node_password',
    'node_secret',
    'node_sha1',
    'node_ssrf',
    'node_timing_attack',
    'node_tls_reject',
    'node_weak_crypto',
    'node_xpath_injection',
    'node_xxe',
    'yaml_deserialize',
    'yaml_deserialize2',
    'zip_path_overwrite',
    'zip_path_overwrite2',
    'admzip_path_overwrite',
    'tar_path_overwrite',
    'electron_disable_websecurity',
    'electron_allow_http',
    'electron_blink_integration',
    'electron_nodejs_integration',
    'electron_context_isolation',
    'electron_experimental_features',
    'squirrelly_autoescape',
    'server_side_template_injection',
    'node_error_disclosure',
    'generic_error_disclosure',
    'node_logic_bypass',
    'regex_injection_dos',
]

CONTROLS = [
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
]


def test_nodejs():
    paths = get_paths('nodejs')
    truepos = paths['true_positives']
    res = scanner([truepos], False)
    assert len(res['nodejs'].keys()) != 0


def test_nodejs_rules():
    paths = get_paths('nodejs')
    truepos = paths['true_positives']
    trueneg = paths['true_negatives']
    pos_files = list(truepos.glob('**/*.js'))
    neg_files = list(trueneg.glob('**/*.js'))
    assert len(pos_files) == len(neg_files)
    res = scanner(pos_files, True)
    actual = [*res['nodejs']]
    actual.sort()
    EXPECTED.extend(CONTROLS)
    EXPECTED.sort()
    assert actual == EXPECTED
    res = scanner(neg_files, True)
    assert res['nodejs'] == {}
