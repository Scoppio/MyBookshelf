import atexit
from bookshelf._reposiroty.repository_inmemory import close_db
from bookshelf._reposiroty.repository import get, save_new_item, update_item
atexit.register(close_db)

__all__ = ['get', 'save_new_item', 'update_item']