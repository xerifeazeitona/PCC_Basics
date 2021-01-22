# 7-10. Dream Vacation
# Write a program that polls users about their dream vacation.
# Write a prompt similar to If you could visit one place in the world,
# where would you go? Include a block of code that prints the results
# of the poll.
locations = []

prompt = "\nIf you could visit one place in the world, where would you go?"
prompt += "\n('q' to quit) "

while True:
    location = input(prompt)

    if location == 'q':
        break
    else:
        print(f"{location.title()} added to the poll results")
        locations.append(location)

print("\n-=-=-=-Poll results-=-=-=-")
for location in locations:
    print(f"- {location.title()}")
