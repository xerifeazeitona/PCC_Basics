# 6-9. Favorite Places
# Make a dictionary called favorite_places. Think of three names to use
# as keys in the dictionary, and store one to three favorite places for
# each person.
favorite_places = {
    'sarah': ['library','cafe'],
    'phill': ['casino'],
    'carla': ['park','mountain','beach'],
}

# Loop through the dictionary, and print each person’s name and their
# favorite places.
for name, places in favorite_places.items():
    if len(places) > 1:
        print(f"\n{name.title()}'s favorite places are:")
        for place in places:
            print(f"\t- {place}")
    else:
        print(f"\n{name.title()}'s favorite place is:\n\t- " \
            f"{places[0]}")
