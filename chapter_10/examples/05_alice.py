"""
One common issue when working with files is handling missing files.
The file you’re looking for might be in a different location, the
filename may be misspelled, or the file may not exist at all.
You can handle all of these situations in a straightforward way with a
try-except block.
"""
filename =  'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")
