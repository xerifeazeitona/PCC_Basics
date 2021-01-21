# 6-7. People
# Start with the program you wrote for Exercise 6-1.
person_0 = {
    'first_name': 'larry',
    'last_name': 'jules',
    'age': '40',
    'city': 'toronto',
    }

# Make two new dictionaries representing different people,
person_1 = {
    'first_name': 'jenny',
    'last_name': 'tahglia',
    'age': '21',
    'city': 'montreal',
    }

person_2 = {
    'first_name': 'holden',
    'last_name': 'makok',
    'age': '69',
    'city': 'vancouver',
    }

# and store all three dictionaries in a list called people.
people = [person_0, person_1, person_2]

# Loop through your list of people. As you loop through the list, print
# everything you know about each person.
for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"\nFull name: {full_name.title()}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city'].title()}")
    