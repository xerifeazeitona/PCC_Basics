# To make a slice, you specify the index of the first and last elements
# you want to work with
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# You can generate any subset of a list
print(players[1:4])

# If you omit the first index in a slice, Python automatically starts
# your slice at the beginning of the list
print(players[:4])

# A similar syntax works if you want a slice that includes the end of a
# list
print(players[2:])

# You can use a slice in a for loop if you want to loop through a subset
# of the elements in a list
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())