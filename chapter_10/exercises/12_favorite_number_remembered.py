"""
10-12. Favorite Number Remembered
Combine the two programs from Exercise 10-11 into one file.
If the number is already stored, report the favorite number to the user.
If not, prompt for the user’s favorite number and store it in a file.
Run the program twice to see that it works.
"""

import json

def get_saved_number():
    """Tries to retrieve the saved number."""
    filename = 'favorite_number.json'
    try:
        with open(filename) as f:
            saved_number = json.load(f)
        return saved_number
    except FileNotFoundError:
        return None

def get_number():
    """Prompt for favorite number."""
    new_number = input("What's your favorite number? ")
    with open('favorite_number.json', 'w') as f:
        json.dump(new_number, f)
    print("Now I know your favorite number!")


number = get_saved_number()
if number:
    print(f"I know your favorite number! It's {number}.")
else:
    get_number()
