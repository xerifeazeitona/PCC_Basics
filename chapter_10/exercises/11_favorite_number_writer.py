"""
10-11. Favorite Number
Write a program that prompts for the user’s favorite number.
Use json.dump() to store this number in a file.
"""

import json

number = input("What's your favorite number? ")

with open('favorite_number.json', 'w') as f:
    json.dump(number, f)

print("Now I know your favorite number!")
