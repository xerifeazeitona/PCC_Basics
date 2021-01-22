"""
8-11. Archived Messages
Start with your work from Exercise 8-10.
Call the function send_messages() with a copy of the list of messages.
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
sent_msgs = send_messages(short_messages[:])

# After calling the function, print both of your lists to show that the
# original list has retained its messages.
print(short_messages)
print(sent_msgs)
