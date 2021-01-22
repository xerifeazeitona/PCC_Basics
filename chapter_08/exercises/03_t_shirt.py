"""
8-3. T-Shirt
Write a function called make_shirt() that accepts a size and the text
of a message that should be printed on the shirt. The function should
print a sentence summarizing the size of the shirt and the message
printed on it.
"""
def make_shirt(size, message):
    """
    Prints a sentence summarizing the size of the shirt and the 
    message being printed on it.
    """
    print(f'{size.title()} size with the message "{message}" printed on it.')

# Call the function once using positional arguments to make a shirt.
make_shirt('small', 'Hello world!')
# Call the function a second time using keyword arguments.
make_shirt(message='Hello world!', size='small')
