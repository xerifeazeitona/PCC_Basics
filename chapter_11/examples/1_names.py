"""
Propmts for a first and last name, then return a neatly formatted full
name.
"""

from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("\nPlease give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"Neatly formatted name: {formatted_name}.")
