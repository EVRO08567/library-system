class Loan:
    def __init__(self, book, user):
        self.book = book
        self.user = user
        self.is_returned = False

class LoanManager:
    def __init__(self):
        self.loans = []

    def lend_book(self, loan):
        if loan.book.is_available:
            loan.book.is_available = False
            self.loans.append(loan)
            return True
        return False

    def return_book(self, loan):
        loan.book.is_available = True
        loan.is_returned = True

    def get_active_loans(self):
        return [loan for loan in self.loans if not loan.is_returned]
