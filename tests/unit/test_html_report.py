"""HTML report must escape every cell."""
from njsscan.formatters.cli import format_table

PAYLOAD = '<img src=x onerror=alert(1)>'


def finding(description):
    return {
        'metadata': {
            'id': 'rule',
            'description': description,
            'severity': 'ERROR',
            'cwe': ['cwe-79', '<b>'],
        },
        'files': [{
            'file_path': 'src/<i>.js',
            'match_position': (1, 2),
            'match_lines': (3, 3),
            'match_string': '<script>x</script>',
        }],
    }


def test_every_cell_escaped_in_html():
    html = format_table('<rule>', finding(PAYLOAD), 'unsafehtml')
    assert PAYLOAD not in html
    assert '&lt;img src=x onerror=alert(1)&gt;' in html
    for raw in ('<rule>', '<b>', '<i>', '<script>'):
        assert raw not in html
    # The nested files table and the <pre> wrapper are still markup.
    assert html.count('<table>') == 2
    assert '<pre>&lt;script&gt;x&lt;/script&gt;</pre>' in html


def test_text_formats_unchanged():
    out = format_table('rule', finding(PAYLOAD), 'fancy_grid')
    assert PAYLOAD in out
    assert '<script>x</script>' in out
