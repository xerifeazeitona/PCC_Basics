"""
8-9. Messages
Make a list containing a series of short text messages. Pass the list to
a function called show_messages(), which prints each text message.
"""
def show_messages(messages):
    """Prints a list of messages."""
    for message in messages:
        print(message)

short_messages = [
    'Hello world!',
    'Apples and oranges...',
    'The robots are coming!'
]
show_messages(short_messages)
