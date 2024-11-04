"""Test Node.js rules."""
from .setup_test import (
    get_paths,
    scanner,
)

from njsscan.formatters import (
    json_out,
    sarif,
    sonarqube,
)


TRIGGERED = {
    'zip_path_overwrite2': 1,
    'zip_path_overwrite': 3,
    'tar_path_overwrite': 2,
    'admzip_path_overwrite': 2,
    'generic_os_command_exec': 10,
    'server_side_template_injection': 5,
    'node_error_disclosure': 1,
    'node_ssrf': 11,
    'node_xpath_injection': 4,
    'node_entity_expansion': 1,
    'express_xss': 17,
    'node_xxe': 5,
    'eval_nodejs': 4,
    'header_xss_generic': 6,
    'generic_path_traversal': 6,
    'express_open_redirect2': 5,
    'express_open_redirect': 15,
    'generic_header_injection': 17,
    'express_cors': 6,
    'node_aes_ecb': 5,
    'node_aes_noiv': 2,
    'node_sha1': 1,
    'node_md5': 1,
    'node_insecure_random_generator': 2,
    'node_weak_crypto': 1,
    'node_timing_attack': 6,
    'node_logic_bypass': 1,
    'regex_injection_dos': 1,
    'regex_dos': 6,
    'generic_error_disclosure': 2,
    'express_bodyparser': 1,
    'layer7_object_dos': 2,
    'node_deserialize': 1,
    'serializetojs_deserialize': 2,
    'yaml_deserialize': 3,
    'hardcoded_jwt_secret': 19,
    'node_secret': 11,
    'node_password': 9,
    'node_username': 1,
    'node_api_key': 7,
    'generic_cors': 1,
    'helmet_feature_disabled': 2,
    'header_xss_lusca': 2,
    'node_jwt_none_algorithm': 2,
    'electron_disable_websecurity': 3,
    'electron_allow_http': 2,
    'electron_blink_integration': 1,
    'electron_nodejs_integration': 1,
    'electron_context_isolation': 1,
    'electron_experimental_features': 1,
    'node_tls_reject': 2,
    'node_curl_ssl_verify_disable': 1,
    'handlebars_safestring': 3,
    'handlebars_noescape': 2,
    'squirrelly_autoescape': 1,
    'node_sqli_injection': 6,
    'node_knex_sqli_injection': 4,
    'node_nosqli_injection': 5,
    'node_nosqli_js_injection': 3,
    'host_header_injection': 12,
    'xxe_xml2json': 2,
    'vm_code_injection': 3,
    'vm_runincontext_injection': 2,
    'vm_runinnewcontext_injection': 2,
    'vm_compilefunction_injection': 1,
    'vm2_code_injection': 3,
    'vm2_context_injection': 2,
    'xss_serialize_javascript': 2,
    'xxe_sax': 2,
    'xxe_expat': 3,
    'sandbox_code_injection': 3,
    'puppeteer_ssrf': 5,
    'phantom_ssrf': 12,
    'wkhtmltopdf_ssrf': 1,
    'wkhtmltoimage_ssrf': 1,
    'hardcoded_passport_secret': 13,
    'grpc_insecure_connection': 3,
    'jwt_express_hardcoded': 5,
    'jwt_exposed_credentials': 14,
    'jwt_exposed_data': 3,
    'jwt_not_revoked': 5,
    'buffer_noassert': 1,
    'xss_disable_mustache_escape': 1,
    'join_resolve_path_traversal': 4,
    'eval_require': 4,
    'cookie_session_default': 1,
    'cookie_session_no_secure': 1,
    'cookie_session_no_samesite': 1,
    'cookie_session_no_httponly': 1,
    'cookie_session_no_domain': 1,
    'cookie_session_no_path': 1,
    'cookie_session_no_maxage': 1,
    'shelljs_os_command_exec': 2,
    'playwright_ssrf': 5,
    'express_lfr': 1,
    'express_lfr_warning': 2,
    'sequelize_tls': 4,
    'sequelize_tls_cert_validation': 3,
    'sequelize_weak_tls': 4,
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
    json_output(res)
    sonar_output(res)
    sarif_output(res)


def nodejs_rule_trigger_count(res):
    TRIGGERED.update(CONTROLS)
    actual = {}
    for rule_id, det in res['nodejs'].items():
        actual[rule_id] = len(det.get('files', []))
    assert TRIGGERED == actual


def json_output(res):
    jout = json_out.json_output(None, res, '0.0.0')
    assert jout is not None


def sonar_output(res):
    sonar_out = sonarqube.sonarqube_output(None, res, '0.0.0')
    assert sonar_out is not None


def sarif_output(res):
    sarif_out = sarif.sarif_output(None, res, '0.0.0')
    assert sarif_out is not None
