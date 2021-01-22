"""
8-4. Large Shirts
Modify the make_shirt() function so that shirts are large by default
with a message that reads "I love Python".
"""
def make_shirt(size='large', message='I love Python'):
    """
    Prints a sentence summarizing the size of the shirt and the 
    message being printed on it.
    """
    print(f'{size.title()} size with the message "{message}" printed on it.')

# Make a large shirt and a medium shirt with the default message, and
# a shirt of any size with a different message.
make_shirt()
make_shirt('medium')
make_shirt('x-small', 'One tiny boi')
