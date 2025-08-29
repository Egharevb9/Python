import json
import os



books = []

def add_book(title, author):
    books.append({"title": title, "author": author, "available": True})

def get_books():
    return books

file_path = "library_data.json"
books = []


def load_books():
    """load books from JSON file if it exists"""
    global books
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            books = json.load(f)
    else:
        books= []


def save_books():
    """save current books list to JSON file"""
    with open(file_path, "W")as f:
        json.dump(books,f, indent=4)


def add_book(title,author):
    books.append({"title":title, "author":author, "available": True})
    save_books()

def get_books():
    return    


