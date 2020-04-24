"""Test Setup."""
from pathlib import Path

from njsscan.njsscan import NJSScan


def scanner(paths):
    return NJSScan(paths, True).scan()


def get_paths():
    base_dir = Path(__file__).parents[1]
    dot_file = base_dir / 'assets' / 'dot_njsscan'
    js_dir = base_dir / 'assets' / 'node_source'
    template_files = base_dir / 'assets' / 'templates'
    true_positves = js_dir / 'true_positives'
    true_negatives = js_dir / 'true_negatives'
    paths = {
        'dot_file': dot_file,
        'js_dir': js_dir,
        'template_files': template_files,
        'true_positives': true_positves,
        'true_negatives': true_negatives,
    }
    return paths
