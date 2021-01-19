# 3-7. Shrinking Guest List
# You just found out that your new dinner table won’t arrive in time for
# the dinner, and you have space for only two guests.

# Start with your program from Exercise 3-6. 
persons = []
persons.append('jenny')
persons.append('grace')
persons.append('fred')
persons.insert(0, 'chris')
persons.insert(2, 'mark')
persons.append('sarah')
for person in persons:
    print(f"Hello {person.title()}, would you like to come for dinner?")

# Add a new line that prints a message saying that you can invite only
# two people for dinner.
message = "\nLooks like I can only invite two people, sorry!\n"
print(message)

# Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list,
# print a message to that person letting them know you’re sorry you can’t
# invite them to dinner.
while len(persons) > 2:
    uninvited_guest = persons.pop()
    print(f"{uninvited_guest.title()}, sorry but you're uninvited...")

# Print a message to each of the two people still on your list, letting
# them know they’re still invited.
for person in persons:
    print(f"{person.title()}, you're still invited!")

# Use del to remove the last two names from your list, so you have an
# empty list. Print your list to make sure you actually have an empty
# list at the end of your program.
while persons:
    del persons[0]
print(persons)