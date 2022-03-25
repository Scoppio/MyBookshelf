from typing import List, Optional
from bookshelf.models import Book
from bookshelf._reposiroty import repository_inmemory, repository_fs
from bookshelf.feature_toggle import flag_value
from bookshelf import get_current_context, setup_and_get_logger

logger = setup_and_get_logger(__name__)


def get(size: int, offset: int, tag: Optional[str] = None) -> List[Book]:
    if flag_value('NewDatabase', False, context=get_current_context()):
        logger.info("Using in memory DB")
        books = repository_inmemory.get(size, offset)
    else:
        logger.info("Using in file DB")
        books = repository_fs.get(size, offset)

    books = list(filter(lambda book: tag in book.tags, books))

    return books


def save_new_item(book: Book):
    repository_inmemory.save_new_item(book)
    repository_fs.save_new_item(book)


def update_item(book: Book):
    repository_inmemory.update_item(book)
    repository_fs.update_item(book)

