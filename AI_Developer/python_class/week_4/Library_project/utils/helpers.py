# utils/helpers.py - this will handle helper functions

def format_book(book):
    status = "Availiable" if book["available"] else "Borrowed"
    return f"{book['title']} by {book['author']} - {status}"


def format_book(book,index):
    status = "available" if book["available"] else "Borrowed"
    return f"{index}.{book['title']} by {book['author']} - {status}"