# 6-6. Polling: 
# Use the code in favorite_languages.py.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print()
# Make a list of people who should take the favorite languages poll.
# Include some names that are already in the dictionary and some that
# are not.
people = ['kyle', 'sarah', 'phil', 'diana']

# Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to
# take the poll.
for person in people:
    if person in favorite_languages:
        print(f"{person.title()}, thank you for taking the poll.")
    else:
        print(f"{person.title()}, please take our poll!")
        