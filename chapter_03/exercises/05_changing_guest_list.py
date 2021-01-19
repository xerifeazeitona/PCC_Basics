# 3-5. Changing Guest List
# You just heard that one of your guests can’t make the dinner, so you
# need to send out a new set of invitations. You’ll have to think of
# someone else to invite.

# Start with your program from Exercise 3-4. Add a print() call at the
# end of your program stating the name of the guest who can’t make it.
persons = []
persons.append('jenny')
persons.append('grace')
persons.append('fred')

for person in persons:
    print(f"Hello {person.title()}, would you like to come for dinner?")

print(f"\nLooks like {persons[0].title()} can't make it...\n")

# Modify your list, replacing the name of the guest who can’t make it
# with the name of the new person you are inviting.
persons[0] = 'paula'

# Print a second set of invitation messages, one for each person who is
# still in your list.
for person in persons:
    print(f"Hello {person.title()}, would you like to come for dinner?")
