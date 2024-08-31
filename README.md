# Library Management System

## Overview

This project is a simple Library Management System implemented in Python. It provides basic functionalities to manage books in a library, including adding new books, borrowing books, returning books, and viewing available books. The system uses object-oriented principles and includes test cases to verify the functionality.

## Files

1. **`library_management_system.py`**:
   - Contains the implementation of the `LibraryBook` and `LibraryManagement` classes.
   - The `LibraryBook` class represents a book with attributes like ISBN, title, author, and publication year.
   - The `LibraryManagement` class manages a collection of books with methods to add, borrow, return, and view available books.

2. **`tdd.py`**:
   - Contains unit tests for the `LibraryManagement` class using the `unittest` framework.
   - Tests include adding books, borrowing books, returning books, and viewing available books.

## Usage

1. **Add a New Book**:
   - Create an instance of `LibraryBook` with the desired attributes.
   - Use the `add_new_book` method of `LibraryManagement` to add the book to the library.

2. **Borrow a Book**:
   - Call the `borrow_book` method with the book's ISBN to mark it as borrowed.

3. **Return a Book**:
   - Use the `return_book` method with the book's ISBN to mark it as returned.

4. **View Available Books**:
   - Use the `view_available_books` method to get a list of books that are not currently borrowed.

## Testing

Run the test using `unittest` to verify the functionality of the system:

## Command Prompt
python -m unittest tdd.py
