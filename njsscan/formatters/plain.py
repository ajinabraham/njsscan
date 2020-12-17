# -*- coding: utf_8 -*-
"""Plain njsscan output format."""
from njsscan.logger import init_logger

logger = init_logger(__name__)

def print_tool_info(ver):
    """Tool info."""
    tool_str = '\nnjsscan: v{} | Ajin Abraham | opensecurity.in'.format(ver)
    logger.info(tool_str)
    return tool_str

def format_plain(rule_id, details):
    """Get CLI friendly format."""
    items = []
    items.append('\n==================================================='
                 '===================================================')
    items.append(f'RULE ID: {rule_id}')
    for meta, value in details['metadata'].items():
        if meta == 'id':
            continue
        meta_format = meta.upper().replace('_', '')
        items.append(f'{meta_format}: {value}')
    items.append('==================================================='
                 '===================================================')
    files = details.get('files')
    if not files:
        return '\n'.join(items)
    items.append('\n__________________FILES___________________________')
    for match in files:
        items.append('\n')
        file_path = match['file_path']
        items.append(f'File: {file_path}')
        position = match['match_position']
        items.append(f'Match Position: {position[0]} - {position[1]}')
        lines = match.get('match_lines')
        line = (lines[0] if lines[0] == lines[1]
                else f'{lines[0]}: {lines[1]}')
        items.append(f'Line Number(s): {line}')
        match_string = match['match_string']
        if isinstance(match_string, list):
            match_string = '\n'.join(ln.strip() for ln in match_string)
        items.append(f'Match String: {match_string}')
    return '\n'.join(items)


def plain_output(outfile, scan_results, version):
    """Format output printing."""
    tool = print_tool_info(version)
    if not scan_results:
        return []
    scan_results.pop('errors', None)
    buffer = []
    for out in scan_results:
        for rule_id, details in scan_results[out].items():
            formatted = format_plain(rule_id, details)
            buffer.append(formatted)
            severity = details['metadata']['severity'].lower()
            if not outfile:
                if severity == 'error':
                    logger.error(formatted)
                elif severity == 'warning':
                    logger.warning(formatted)
                else:
                    logger.info(formatted)
    if outfile and buffer:
        buffer.insert(0, tool)
        outdata = '\n'.join(buffer)
        with open(outfile, 'w') as of:
            of.write(outdata)
    return buffer