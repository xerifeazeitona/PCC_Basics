"""
10-13. Verify User
The final listing for remember_me.py assumes either that the user has
already entered their username or that the program is running for the
first time. We should modify it in case the current user is not the
person who last used the program.
Before printing a welcome back message in greet_user(), ask the user if
this is the correct username.
If it’s not, call get_new_username() to get the correct username.
"""

import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        if confirm_username(username):
            return username
        return None

def get_new_username():
    """Prompt for a new username."""
    username = input("What's your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def confirm_username(user):
    """Prompt for confirmation that the username is still current."""
    confirmation = input(f"{user.title()}, is it you? [Y/N] ")
    return confirmation.lower() == 'y'

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username.title()}!")
    else:
        username = get_new_username()
        print(f"We'll remember you next time, {username.title()}!")


greet_user()
