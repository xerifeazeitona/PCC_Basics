"""
There’s no new code here; blocks of code from the last two examples are
just combined into one file.
"""
import json

# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.

filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What's your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username.title()}!")
else:
    print(f"Welcome back, {username.title()}!")
