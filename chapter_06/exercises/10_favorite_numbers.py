# 6-10. Favorite Numbers
# Modify your program from Exercise 6-2 so each person can have more
# than one favorite number.
favorite_numbers = {
    'sarah': [4, 7],
    'james': [7],
    'carla': [2, 5, 8],
    'katie': [3, 4],
    'larry': [8, 3, 5, 1],
    }

# Then print each person’s name along with their favorite numbers.
for name, numbers in favorite_numbers.items():
    if len(numbers) > 1:
        print(f"\n{name.title()}'s favorite numbers are:")
        for number in numbers:
            print(f"\t- {number}")
    else:
        print(f"\n{name.title()}'s favorite number is:\n\t- " \
            f"{numbers[0]}")
