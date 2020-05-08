"""Test Node.js rules."""
from .setup_test import (
    get_paths,
    scanner,
)


TRIGGERED = {
    'zip_path_overwrite2': 1,
    'zip_path_overwrite': 3,
    'tar_path_overwrite': 3,
    'generic_path_traversal3_warning': 5,
    'generic_os_command_exec': 8,
    'server_side_template_injection': 5,
    'node_error_disclosure': 1,
    'node_ssrf': 12,
    'node_xpath_injection': 4,
    'node_entity_expansion': 1,
    'express_xss': 3,
    'node_xxe': 4,
    'eval_nodejs': 4,
    'express_cors2': 3,
    'header_xss_generic': 5,
    'generic_path_traversal2': 2,
    'eval_warning': 4,
    'express_open_redirect2': 5,
    'express_open_redirect': 11,
    'generic_header_injection': 16,
    'express_cors': 5,
    'admzip_path_overwrite': 2,
    'node_aes_ecb': 5,
    'node_sha1': 1,
    'node_md5': 1,
    'node_insecure_random_generator': 2,
    'node_weak_crypto': 1,
    'node_timing_attack': 6,
    'node_logic_bypass': 1,
    'regex_injection_dos': 1,
    'generic_error_disclosure': 2,
    'express_bodyparser': 1,
    'node_deserialize': 2,
    'yaml_deserialize2': 1,
    'yaml_deserialize': 2,
    'hardcoded_jwt_secret': 6,
    'node_secret': 2,
    'node_password': 9,
    'node_api_key': 1,
    'generic_cors': 1,
    'helmet_feature_disabled': 2,
    'header_xss_generic2': 7,
    'header_xss_lusca': 2,
    'node_jwt_none_algorithm': 2,
    'electron_disable_websecurity': 3,
    'electron_allow_http': 3,
    'electron_blink_integration': 1,
    'electron_nodejs_integration': 1,
    'electron_context_isolation': 1,
    'electron_experimental_features': 1,
    'node_tls_reject': 2,
    'node_curl_ssl_verify_disable': 1,
    'handlebars_safestring': 3,
    'handlebars_noescape': 2,
    'squirrelly_autoescape': 1,
}
CONTROLS = {
    'anti_csrf_control': 0,
    'rate_limit_control': 0,
    'helmet_header_hsts': 0,
    'helmet_header_dns_prefetch': 0,
    'helmet_header_x_powered_by': 0,
    'helmet_header_frame_guard': 0,
    'helmet_header_referrer_policy': 0,
    'helmet_header_check_crossdomain': 0,
    'helmet_header_nosniff': 0,
    'helmet_header_check_csp': 0,
    'helmet_header_check_expect_ct': 0,
    'helmet_header_feature_policy': 0,
    'helmet_header_ienoopen': 0,
    'helmet_header_xss_filter': 0,
}


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
    expected = list(TRIGGERED.keys())
    expected.extend(list(CONTROLS.keys()))
    expected.sort()
    assert actual == expected
    neg_res = scanner(neg_files, True)
    assert neg_res['nodejs'] == {}
    nodejs_rule_trigger_count(res)


def nodejs_rule_trigger_count(res):
    TRIGGERED.update(CONTROLS)
    actual = {}
    for rule_id, det in res['nodejs'].items():
        actual[rule_id] = len(det.get('files', []))
    assert TRIGGERED == actual
