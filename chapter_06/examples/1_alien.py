# In Python, a dictionary is wrapped in braces, {}, with a series of 
# key-value pairs inside the braces
alien_0 = {'color': 'green', 'points': 5}

# To get the value associated with a key, give the name of the
# dictionary and then place the key inside a set of square brackets
print(alien_0['color'])
print(alien_0['points'])

# You can add new key-value pairs to a dictionary at any time
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Modifying values in a dictionary
print(f"\nThe alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.\n")

# A more interesting example
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original x-position: {alien_0['x_position']}")

# Move the alien to the right
# Determine how far to move based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

# The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New x-position: {alien_0['x_position']}\n")

# You can use del to remove a key-value pair permanently
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

# You can use the get() method to set a default value that will be
# returned if the requested key doesn't exist
alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.\n')
print(point_value)

# A list of dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# list of dictionaries are useful when creating things automatically
print()
# Make an empty list for storing aliens
aliens = []

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")

# Each created alien is a separate object, so we can modify each alien
# individually
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Show the first 5 aliens again
for alien in aliens[:5]:
    print(alien)
print("...\n")

# You could expand this loop by adding an elif block that turns yellow
# aliens into red
for alien in aliens[:4]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Show the first 5 aliens again
for alien in aliens[:5]:
    print(alien)
print("...\n")
