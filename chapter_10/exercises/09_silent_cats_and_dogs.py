"""
10-9. Silent Cats and Dogs
Modify your except block in Exercise 10-8 to fail silently if either
file is missing.
"""

def print_file_contents(filename):
    """Opens a file, read and print its contents in the screen."""
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        pass

print_file_contents('cats.txt')
print_file_contents('dogs.txt')
