# 6-3. Glossary
# A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store
# their meanings as values.
glossary = {
    'if': 'conditional statement',
    'variable': 'used to store values',
    'list': 'lists of values',
    'int': 'integer',
    'str': 'string',
    }

# Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the
# word on one line and then print its meaning indented on a second line.
# Use the newline character (\n) to insert a blank line between each
# word-meaning pair in your output.
print(f"if: {glossary['if']}\n")
print(f"variable: {glossary['variable']}\n")
print(f"list: {glossary['list']}\n")
print(f"int: {glossary['int']}\n")
print(f"str: {glossary['str']}\n")
