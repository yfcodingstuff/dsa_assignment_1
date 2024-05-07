from book import *
books = {}

def add_book(isbn, title, publisher, language, num_copies, availability):
    new_book = Book(isbn, title, publisher, language, num_copies, availability)
    books[isbn] = new_book

def display_all_books():
    print("\nAll Book Records:")
    for isbn, book in books.items():
        print(f"ISBN: {isbn}, Title: {book.get_title()}, Publisher: {book.get_publisher()}, Language: {book.get_language()}, Number of Copies: {book.get_num_copies()}, Availability: {book.get_availability()}")
        