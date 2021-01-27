"""
10-11. Favorite Number
Write a separate program that reads in this value and prints the
message, “I know your favorite number! It’s _____.”
"""

import json

filename = 'favorite_number.json'
try:
    with open(filename) as f:
        number = json.load(f)
    print(f"I know your favorite number! It's {number}.")
except FileNotFoundError:
    print("Sorry, I can't seem to find your number...")
