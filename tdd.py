import unittest
from library_management_system import LibraryBook, LibraryManagement

class TddForLib(unittest.TestCase):
    def setUp(self):
        self.library_management_system = LibraryManagement()
        self.first_book = LibraryBook("ABC123", "The Art of Computer Programming", "Donald Knuth", 2011)
        self.second_book = LibraryBook("XYZ789", "Computer Networks", "Andrew Tanenbaum", 1981)
        self.third_book = LibraryBook("DEF456", "Atomic habits", "James Clear", 2018)

    def test_add_book(self):
        self.library_management_system.add_new_book(self.first_book)
        self.library_management_system.add_new_book(self.second_book)
        self.library_management_system.add_new_book(self.third_book)

        """Add three books in library"""
        self.assertIn(self.first_book, self.library_management_system.store_books)
        self.assertIn(self.second_book, self.library_management_system.store_books)
        self.assertIn(self.third_book, self.library_management_system.store_books)

    def test_borrow_book(self):
        """Add three books in library"""
        self.library_management_system.add_new_book(self.first_book)
        self.library_management_system.add_new_book(self.second_book)
        self.library_management_system.add_new_book(self.third_book)

        """Here three books are added so we borrow first book from it """
        self.library_management_system.borrow_book("ABC123")
        self.assertTrue(self.first_book.borrowed)

    def test_return_book(self):
        """Add three books in library"""
        self.library_management_system.add_new_book(self.first_book)
        self.library_management_system.add_new_book(self.second_book)
        self.library_management_system.add_new_book(self.third_book)

        """Here three books are added so we borrow first book from it """
        self.library_management_system.borrow_book("ABC123")
        self.assertTrue(self.first_book.borrowed)

        """Here first book is Borrowed so we return that first book """
        self.library_management_system.return_book("ABC123")
        self.assertFalse(self.first_book.borrowed)

    def test_view_available_books(self):
        """Add three books in library"""
        self.library_management_system.add_new_book(self.first_book)
        self.library_management_system.add_new_book(self.second_book)
        self.library_management_system.add_new_book(self.third_book)

        """Here three books are added so we borrow first book from it """
        self.library_management_system.borrow_book("ABC123")

        """Now list of books will pe displayed as first book is borrowed"""
        available_books = self.library_management_system.view_available_books()
        self.assertEqual(len(available_books), 2)
        self.assertIn(self.second_book, available_books)
        self.assertIn(self.third_book, available_books)
        self.assertNotIn(self.first_book, available_books)

if __name__ == "__main__":
    unittest.main()


# import unittest
# from library_management_system import LibraryBook, LibraryManagement

# class TddForLib(unittest.TestCase):
#     def setUp(self):
#         self.library_management_system = LibraryManagement()
#         self.first_book = LibraryBook("ABC123", "The Art of Computer Programming", "Donald Knuth", 2011)
#         self.second_book = LibraryBook("XYZ789", "Computer Networks", "Andrew Tanenbaum", 1981)
#         self.third_book = LibraryBook("DEF456", "Atomic habits", "James Clear", 2018)

#     def add_book_testing(self):
#         self.library_management_system.add_new_book(self.first_book)
#         self.library_management_system.add_new_book(self.second_book)
#         self.library_management_system.add_new_book(self.third_book)

#         """Add three books in library"""

#         self.assertIn("ABC123", self.library_management_system.store_books)
#         self.assertIn("XYZ789", self.library_management_system.store_books)
#         self.assertIn("DEF456", self.library_management_system.store_books)

#     def borrow_book_testing(self):
#         """Add three books in library"""

#         self.library_management_system.add_new_book(self.first_book)
#         self.library_management_system.add_new_book(self.second_book)
#         self.library_management_system.add_new_book(self.third_book)

#         """Here three books are added so we borrow first book from it """
#         self.library_management_system.borrow_book("ABC123")
#         self.assertTrue(self.first_book.borrow)

#     def return_book_testing(self):
#         """Add three books in library"""

#         self.library_management_system.add_new_book(self.first_book)
#         self.library_management_system.add_new_book(self.second_book)
#         self.library_management_system.add_new_book(self.third_book)

#         """Here three books are added so we borrow first book from it """
#         self.library_management_system.borrow_book("ABC123")
#         self.assertTrue(self.first_book.borrow)

#         """Here first book is Borrowed so we return that first book """
#         self.library_management_system.return_book("ABC123")
#         self.assertFalse(self.first_book.borrow)

#     def view_available_book_testing(self):
#         """Add three books in library"""

#         self.library_management_system.add_new_book(self.first_book)
#         self.library_management_system.add_new_book(self.second_book)
#         self.library_management_system.add_new_book(self.third_book)

#         """Here three books are added so we borrow first book from it """
#         self.library_management_system.borrow_book("ABC123")
#         self.assertTrue(self.first_book.borrow)

#         """Now list of books will pe displayed as first book is borrowed"""
#         remaining_books = self.library_management_system.view_available_books()
#         self.assertEqual(len(remaining_books), 2)
#         self.assertEqual(remaining_books[0].isbn, "ABC123")

# if __name__ == "__main__":
#     unittest.main()
