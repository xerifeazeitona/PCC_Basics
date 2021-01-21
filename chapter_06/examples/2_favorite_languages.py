# The previous example involved storing different kinds of information
# about one object, an alien in a game. You can also use a dictionary to
# store one kind of information about many objects

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.\n")

# looping through dictionaries example
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print()
# The keys() method is useful when you don’t need to work with all of
# the values in a dictionary
for name in favorite_languages.keys():
    print(name.title())

print()
# You can access the value associated with any key you care about inside
# the loop by using the current key.
friends = ['phil', 'sarah']

for name in favorite_languages:
    print(f"Hi {name.title()}")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language.title()}!")

# You can also use the keys() method to find out if a particular person
# was polled
if 'erin' not in favorite_languages:
    print("\nErin, please take our poll!\n")

# You can use the sorted() function to get a copy of the keys in order
for name in sorted(favorite_languages):
    print(f"{name.title()}, thank you for taking the poll.")

# You can use the values() method to return a list of values without any
# keys
print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
    print(f"- {language.title()}")

# To see each language chosen without repetition, we can use a set.
# A set is a collection in which each item must be unique
print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(f"- {language.title()}")

# You can nest a list inside a dictionary any time you want more than
# one value to be associated with a single key in a dictionary

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t- {language.title()}")
    else:
        print(f"\n{name.title()}'s favorite language is:\n\t- " \
            f"{languages[0].title()}")
