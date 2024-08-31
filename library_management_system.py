class LibraryBook:
    def __init__(self, isbn, title, author, year_of_publication):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year_of_publication = year_of_publication
        self.borrowed = False

class LibraryManagement:
    def __init__(self):
        self.store_books = []

    def add_new_book(self, book):
        """Add a new book to the library."""
        if book in self.store_books:
            raise ValueError("This book is already present in the library.")
        else:
            self.store_books.append(book)

    def borrow_book(self, isbn):
        """Borrow a book from the library."""
        found_book = False
        for book in self.store_books:
            if book.isbn == isbn:
                found_book = True
                if book.borrowed:
                    raise ValueError("This book is already borrowed.")
                else:
                    book.borrowed = True
                    break
        if not found_book:
            raise ValueError("This book is not available.")

    def return_book(self, isbn):
        """Return a book to the library."""
        found_book = False
        for book in self.store_books:
            if book.isbn == isbn:
                found_book = True
                if not book.borrowed:
                    raise ValueError("This book was not borrowed.")
                else:
                    book.borrowed = False
                    break
        if not found_book:
            raise ValueError("This book is not in the library.")

    def view_available_books(self):
        """View all available books in the library."""
        return [book for book in self.store_books if not book.borrowed]
