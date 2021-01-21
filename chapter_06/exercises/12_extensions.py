# 6-12. Extensions
# We’re now working with examples that are complex enough that they can
# be extended in any number of ways. Use one of the example programs
# from this chapter, and extend it by adding new keys and values,
# changing the context of the program or improving the formatting
# of the output.

# 6-10. Favorite Numbers v2
# Modify your program from Exercise 6-2 so each person can have more
# than one favorite number.
favorite_numbers = {
    'sarah': [4, 7],
    'james': [7],
    'carla': [2, 5, 8],
    'katie': [3, 4],
    'larry': [8, 3, 5, 1],
    }

# Then print each person’s name along with their favorite numbers in the
# same line, separating numbers with commas and using "and" before the
# last number.
for name, numbers in favorite_numbers.items():
    if len(numbers) > 1:
        favorites = ""
        current_number = 1
        last_number = len(numbers)
        for number in numbers:
            if len(favorites) == 0:
                favorites = favorites + f"{number}"
            elif current_number < last_number:
                favorites = favorites + f", {number}"
            else:
                favorites = favorites + f" and {number}"
            current_number += 1
        print(f"\n{name.title()}'s favorite numbers are: {favorites}")
    else:
        print(f"\n{name.title()}'s favorite number is: {numbers[0]}")
