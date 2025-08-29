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