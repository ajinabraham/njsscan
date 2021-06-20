"""Test Setup."""
from pathlib import Path

from njsscan.njsscan import NJSScan


def scanner(paths, check_controls):
    return NJSScan(paths, True, check_controls).scan()


def get_paths(who):
    base_dir = Path(__file__).parents[1]
    dot_file = base_dir / 'assets' / 'dot_njsscan'
    js_dir = base_dir / 'assets' / 'node_source'
    template_dir = base_dir / 'assets' / 'templates'
    if who == 'nodejs':
        true_positves = js_dir / 'true_positives' / 'semantic_grep'
        true_negatives = js_dir / 'true_negatives'
    else:
        true_positves = template_dir / 'true_positives'
        true_negatives = template_dir / 'true_negatives'
    paths = {
        'dot_file': dot_file,
        'js_dir': js_dir,
        'template_dir': template_dir,
        'true_positives': true_positves,
        'true_negatives': true_negatives,
    }
    return paths
