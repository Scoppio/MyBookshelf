import json
import os
from typing import List, Optional, NewType
from bookshelf.models import Book, UID
from bookshelf import RESOURCES_FOLDER

DB = NewType('DB', dict)


def __get_database() -> DB:
    with open(os.path.join(RESOURCES_FOLDER, 'fs.db'), 'r') as fsdb:
        return DB(json.load(fsdb))


def __commit_transaction(db: DB):
    with open(os.path.join(RESOURCES_FOLDER, 'fs.db'), 'w') as fsdb:
        json.dump(db, fsdb, indent=2)


def __revert(db: DB) -> DB:
    return __get_database()


def get(size: int, offset: int) -> List[Book]:
    db = __get_database()
    start = min([len(db['content_list']), offset * size])
    end = min([len(db['content_list']), (offset + 1) * size])
    return [Book(**i) for i in db['content_list'][start:end]]


def get_by_uid(uid: UID) -> Optional[Book]:
    db = __get_database()
    position = db['uid_index'].get(uid)
    if len(db['max_position']) < position:
        return Book(**db['content_list'][position])
    else:
        return None


def save_new_item(book: Book):
    db = __get_database()
    if book.uid in db['uid_index']:
        raise KeyError('Uid already present in the database')

    position = len(db['content_list'])
    db['uid_index'][book.uid] = position
    db['content_list'].append(book.__dict__)
    __commit_transaction(db)


def update_item(book: Book):
    db = __get_database()
    if book.uid not in db['uid_index']:
        raise KeyError('Uid not present in the database')

    position = db['uid_index'][book.uid]
    db['content_list'][position] = book.__dict__
    __commit_transaction(db)
