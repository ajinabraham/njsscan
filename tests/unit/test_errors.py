"""Test that files njsscan could not scan are not reported as a clean run."""
import json

import pytest

from njsscan.__main__ import handle_exit
from njsscan.formatters import (
    gitlab_sast,
    json_out,
    sarif,
)
from njsscan.njsscan import NJSScan


SINK = (
    "const cp = require('child_process');\n"
    "app.get('/run', function (req, res) {\n"
    "  cp.exec('ls ' + req.query.dir, function (err, out) {\n"
    '    res.send(out);\n'
    '  });\n'
    '});\n'
)
UNPARSEABLE = 'function other( {\n\n' + SINK


def scan(path):
    return NJSScan([str(path)], True, False).scan()


def test_unparseable_file_is_an_error(tmp_path):
    (tmp_path / 'broken.js').write_text(UNPARSEABLE)
    result = scan(tmp_path)

    # The same code parses, so the sink itself is detectable.
    assert result['errors']
    assert not result['nodejs']

    with pytest.raises(SystemExit) as exit_info:
        handle_exit(result, False)
    assert exit_info.value.code == 1

    report = json.loads(sarif.sarif_output(None, result, '0.0.0'))
    assert not report['runs'][0]['invocations'][0]['executionSuccessful']

    gitlab = json.loads(gitlab_sast.gitlab_sast_output(None, result, '0.0.0'))
    assert gitlab['scan']['status'] == 'failure'

    dumped = json.loads(json_out.json_output(None, result.copy(), '0.0.0'))
    assert dumped['errors']
    assert dumped['nodejs'] == {}


def test_parseable_file_is_not_an_error(tmp_path):
    (tmp_path / 'ok.js').write_text(SINK)
    result = scan(tmp_path)

    assert not result['errors']
    assert 'generic_os_command_exec' in result['nodejs']

    report = json.loads(sarif.sarif_output(None, result, '0.0.0'))
    assert report['runs'][0]['invocations'][0]['executionSuccessful']

    gitlab = json.loads(gitlab_sast.gitlab_sast_output(None, result, '0.0.0'))
    assert gitlab['scan']['status'] == 'success'

    dumped = json.loads(json_out.json_output(None, result.copy(), '0.0.0'))
    assert not dumped['errors']
    assert 'generic_os_command_exec' in dumped['nodejs']


def test_clean_file_exits_zero(tmp_path):
    (tmp_path / 'ok.js').write_text('const a = 1;\n')
    result = scan(tmp_path)

    assert not result['errors']
    assert not result['nodejs']

    with pytest.raises(SystemExit) as exit_info:
        handle_exit(result, False)
    assert exit_info.value.code == 0
