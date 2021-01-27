"""
Working with multiple files
"""
def count_words(filename):
    """Count the approximate number of words in a file."""

    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} could not be found.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

books = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for book in books:
    count_words(book)

###
# Lazy note: In the previous example, we informed our users that one of
# the files was unavailable. But you don’t need to report every 
# exception you catch.
# Sometimes you’ll want the program to fail silently when an exception
# occurs and continue on as if nothing happened. To make a program fail
# silently, you write a try block as usual, but you explicitly tell
# Python to do nothing in the except block.
# Python has a pass statement that tells it to do nothing in a block
###