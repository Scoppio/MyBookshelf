from bookshelf import RESOURCES_FOLDER
import json
import os
from typing import Optional, Any
from random import random


def flag_value(name: str, default_value: Optional[Any] = None, context: Optional[dict] = None):
    with open(os.path.join(RESOURCES_FOLDER, 'featuretoggle.json'), 'r') as f:
        flags = json.load(f)
    flag = flags.get(name, dict(value=default_value) if default_value else None)
    if flag:
        if context['user_group'] in flag:
            return __random_value(flag[context['user_group']]['value'])
        return __random_value(flag['value'])
    else:
        return False


def __random_value(value):
    r = value[0]
    p = value[1]
    if random() <= p:
        return r
    return not r
