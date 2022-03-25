import connexion
import os
from pathlib import Path
import logging
import os
import sys

LOGGING_LEVEL = os.getenv('LOGGING_LEVEL', 'INFO').upper()


formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(message)s')
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)


def setup_and_get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(LOGGING_LEVEL)
    logger.addHandler(handler)
    logger.propagate = False  # to prevent log duplication in lambda
    return logger


RESOURCES_FOLDER = os.path.join(Path(__file__).parent, 'resources')

current_context = None

def get_user_groups():
    global current_context
    current_context = connexion.request.headers.get('X-user-group')


def get_current_context():
    return dict(user_group=current_context)


__all__ = ['RESOURCES_FOLDER', 'get_user_groups', 'get_current_context', 'setup_and_get_logger']
