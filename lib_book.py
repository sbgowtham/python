from simpleapi import Bookstore


class LibraryManager:
    def __init__(self, bookstore):
        self.bookstore = bookstore

    def add_book_to_store(self, id, title, author, year, genre):
        new_book = self.bookstore.add_book(id, title, author, year, genre)
        return new_book


if __name__ == "__main__":
    bookstore = Bookstore()

    manager = LibraryManager(bookstore)

    manager.add_book_to_store(1, "The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction")

    print(bookstore.get_book_by_id(1)["title"])
