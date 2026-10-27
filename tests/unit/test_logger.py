"""Unit Tests - logger."""
import logging

from njsscan.logger import init_logger


def test_disabled_level_is_a_noop():
    logger = init_logger('njsscan.tests.disabled')
    logging.getLogger('njsscan.tests.disabled').setLevel(logging.ERROR)
    logger.warning('not shown %s', 1)
    logger.info('not shown')
