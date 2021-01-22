"""
8-2. Favorite Book
Write a function called favorite_book() that accepts one parameter,
title. The function should print a message, such as "One of my favorite
books is Alice in Wonderland."
"""
def favorite_book(book_title):
    """Prints a message about favorite books"""
    print(f"One of my favorite books is {book_title}.")

# Call the function, making sure to include a book title as an argument
# in the function call.
book = "The Return of the King"
favorite_book(book)
