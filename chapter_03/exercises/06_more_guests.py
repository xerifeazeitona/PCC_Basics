# 3-6. More Guests
# You just found a bigger dinner table, so now more space is available.
# Think of three more guests to invite to dinner.

# Start with your program from Exercise 3-4 or Exercise 3-5. 
persons = []
persons.append('jenny')
persons.append('grace')
persons.append('fred')

for person in persons:
    print(f"Hello {person.title()}, would you like to come for dinner?")

# Add a print() call to the end of your program informing people that you
# found a bigger dinner table.
print("\nI've managed to find a bigger dinner table!\n")

# Use insert() to add one new guest to the beginning of your list.
persons.insert(0, 'chris')

# Use insert() to add one new guest to the middle of your list.
persons.insert(2, 'mark')

# Use append() to add one new guest to the end of your list.
persons.append('sarah')

# Print a new set of invitation messages, one for each person in your list.
for person in persons:
    print(f"Hello {person.title()}, would you like to come for dinner?")

