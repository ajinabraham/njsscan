# -*- coding: utf_8 -*-
"""Logger Config."""
import logging


def init_logger(module_name) -> logging.Logger:
    """Setup logger."""
    log_format = ('[%(levelname)s] - '
                  '%(asctime)-15s - '
                  '%(name)s - '
                  '%(message)s')
    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        handlers=[logging.StreamHandler()])
    logger = logging.getLogger(module_name)
    return logger
