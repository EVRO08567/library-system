from books import Book, BookManager
from search import search_by_title, search_by_author
from users import User, UserManager
from loans import Loan, LoanManager
from validators import is_valid_isbn

def main():
    print("=== Library System ===")
    book_manager = BookManager()
    user_manager = UserManager()
    loan_manager = LoanManager()

    # Пример работы
    book = Book("Python Crash Course", "Eric Matthes", "9781593279288")
    if is_valid_isbn(book.isbn):
        book_manager.add_book(book)
        print(f"Book added: {book.title}")

    user = User("Иван", "U001")
    user_manager.add_user(user)

    loan = Loan(book, user)
    if loan_manager.lend_book(loan):
        print(f"Book '{book.title}' lent to {user.name}")

    book_manager.list_books()

if __name__ == "__main__":
    main()
