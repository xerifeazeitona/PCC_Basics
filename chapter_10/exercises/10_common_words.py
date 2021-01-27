"""
10-10. Common Words
Visit [Project Gutenberg](https://gutenberg.org/) and find a few texts
you’d like to analyze. Download the text files for these works, or copy
the raw text from your browser into a text file on your computer.
Write a program that reads the files you found at Project Gutenberg and
determines how many times the word 'the' appears in each text.
This will be an approximation because it will also count words such as
'then' and 'there'. Try counting 'the ', with a space in the string,
and see how much lower your count is.
"""
def count_word(filename, word):
    """Count the approximate number a specific word appears in a file"""

    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} could not be found.")
    else:
        word_count = contents.lower().count(word)
        print(f"The word '{word}' appears around {word_count} times in the " \
            f"file {filename}.")

books = ['jekyll_and_hyde.txt', 'sherlock_holmes.txt']
for book in books:
    count_word(book, 'the')
    count_word(book, 'the ')
