"""Test isolation between configuration reads without starting a scanner."""
import pytest

from njsscan import settings
from njsscan.utils import get_config


@pytest.mark.parametrize('key,setting', [
    ('nodejs-extensions', 'NODEJS_FILE_EXTENSIONS'),
    ('template-extensions', 'TEMPLATE_FILE_EXTENSIONS'),
    ('ignore-filenames', 'IGNORE_FILENAMES'),
    ('ignore-extensions', 'IGNORE_EXTENSIONS'),
    ('ignore-paths', 'IGNORE_PATHS'),
])
def test_config_collections_are_isolated(tmp_path, monkeypatch, key, setting):
    """A custom config must not change defaults or another config's options."""
    defaults = getattr(settings, setting).copy()
    monkeypatch.setattr(settings, setting, defaults.copy())
    first_config = tmp_path / 'first.yaml'
    second_config = tmp_path / 'second.yaml'
    first_config.write_text(f'{key}: [custom-one]\n', encoding='utf-8')
    second_config.write_text(f'{key}: [custom-two]\n', encoding='utf-8')
    option_key = key.replace('-', '_')

    first = get_config([str(tmp_path)], first_config)
    second = get_config([str(tmp_path)], second_config)
    unconfigured = get_config([str(tmp_path)], False)

    assert first[option_key] == defaults | {'custom-one'}
    assert second[option_key] == defaults | {'custom-two'}
    assert unconfigured[option_key] == defaults
    assert getattr(settings, setting) == defaults
