from dataclasses import dataclass
from typing import List, AnyStr, NewType

UID = NewType('UID', int)
Color = NewType('Color', str)
UriRef = NewType('UriRef', str)


@dataclass
class Book:
    uid: UID
    name: AnyStr
    uri: UriRef
    icon: UriRef
    color: AnyStr
    tags: List[AnyStr]
    created_at: AnyStr
    last_modified: AnyStr
