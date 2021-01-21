# 6-4. Glossary 2
# Now that you know how to loop through a dictionary, clean up the code
# from Exercise 6-3 by replacing your series of print() calls with a 
# loop that runs through the dictionary’s keys and values. 
glossary = {
    'if': 'conditional statement',
    'variable': 'used to store values',
    'list': 'lists of values',
    'int': 'integer',
    'str': 'string',
    }

for term, definition in sorted(glossary.items()):
    print(f"{term}: {definition}")

print()
# When you’re sure that your loop works, add five more Python terms to
# your glossary.
glossary['tuple'] = 'an immutable list'
glossary['dictionary'] = 'collection of key-value pairs'
glossary['boolean'] = 'value of a conditional expression after being evaluated'
glossary['comments'] = 'should be limited to 72 characters per line'
glossary['code'] = 'should be limited to 79 characters per line'

# When you run your program again, these new words and meanings should
# automatically be included in the output.
for term, definition in sorted(glossary.items()):
    print(f"{term}: {definition}")
