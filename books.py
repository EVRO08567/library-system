class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, isbn):
        self.books = [b for b in self.books if b.isbn != isbn]

    def list_books(self):
        for b in self.books:
            print(f"{b.title} by {b.author} (ISBN: {b.isbn}) - Available: {b.is_available}")

    def check_availability(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b.is_available
        return False
