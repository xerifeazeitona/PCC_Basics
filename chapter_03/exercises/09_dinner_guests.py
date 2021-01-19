# 3-9. Dinner Guests
# Working with one of the programs from Exercises 3-4 through 3-7, use
# len() to print a message indicating the number of people you are
# inviting to dinner.

persons = []
persons.append('jenny')
persons.append('grace')
persons.append('fred')

for person in persons:
    print(f"Hello {person.title()}, would you like to be one of the " \
        f"{len(persons)} persons I'm inviting for dinner?")