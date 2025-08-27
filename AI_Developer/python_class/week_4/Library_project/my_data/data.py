books = []

def add_book(title, author):
    books.append({"title": title, "author": author, "available": True})

def get_books():
    return books

# utils/helpers.py - this will handle helper functions

def format_book(book):
    status = "Availiable" if book["available"] else "Borrowed"
    return f"{book['title']} by {book['author']} - {status}"


# services/library.py - this will handle helper functions
import my_data.data as data

def borrow_book(title):
    for book in data.get_books():
     if  book["title"].lower() == title.lower() and book["available"]:
             book["available"] = False
             return f"you have borrowed '{book['title']}'"
     return  "Book not available"
    

# main.py - this will be our project entry point

from my_data import data
from utils import  helpers
from services import library

# add some books
data.add_book("python Basic", "John Doe")
data.add_book("advanced python", "Jane smith")

# Display all books
print("library collection :")
for b in my_data.get_books():
    print(helpers.format_book(b))

 # Borrow a book
print("\nBorrowing a book: ")
print(library.borrow_book("python Basic")) 