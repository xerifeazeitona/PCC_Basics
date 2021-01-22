"""
8-10. Sending Messages
Start with a copy of your program from Exercise 8-9.
Write a function called send_messages() that prints each text message
and moves each message to a new list called sent_messages as it’s
printed.
"""
def show_messages(messages):
    """Prints a list of messages."""
    for message in messages:
        print(message)

def move_messages(origin, destination):
    """Move all messages from origin to destination"""
    origin.reverse()
    while origin:
        msg = origin.pop()
        destination.append(msg)

def send_messages(message_list):
    """
    Prints each messsage in the list and moves each message to a new
    list called sent_messages
    """
    sent_messages = []
    # prints each message
    show_messages(message_list)
    # Moves all messages
    move_messages(message_list, sent_messages)
    return sent_messages

short_messages = [
    'Hello world!',
    'Apples and oranges...',
    'The robots are coming!'
]
sent_msgs = send_messages(short_messages)

# After calling the function, print both of your lists to make sure the
# messages were moved correctly.
print(short_messages)
print(sent_msgs)
