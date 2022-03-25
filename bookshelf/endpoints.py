import bookshelf._reposiroty.repository as repository
# from bookshelf import repository
from bookshelf.models import Book


def get_books(size, page, tag):
    return dict(contents=[book.__dict__ for book in repository.get(offset=page, size=size, tag=tag)], size=size, page=page)


def post_books(body):
    return repository.save_new_item(Book(**body))


def put_books(body):
    return repository.update_item(Book(**body))
