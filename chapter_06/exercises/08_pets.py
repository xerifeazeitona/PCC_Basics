# 6-8. Pets
# Make several dictionaries, where each dictionary represents a
# different pet. In each dictionary, include the kind of animal and the
# owner’s name.
pet_0 = {
    'name': 'lady',
    'kind': 'dog',
    'owner': 'mary',
}

pet_1 = {
    'name': 'fluffers',
    'kind': 'cat',
    'owner': 'luke',
}

pet_2 = {
    'name': 'polly',
    'kind': 'bird',
    'owner': 'susan',
}

# Store these dictionaries in a list called pets. 
pets = [pet_0, pet_1, pet_2]

# Next, loop through your list and as you do, print everything you
# know about each pet.
for pet in pets:
    print(f"\nName: {pet['name'].title()}")
    print(f"Kind: {pet['kind'].title()}")
    print(f"Owner: {pet['owner'].title()}")
