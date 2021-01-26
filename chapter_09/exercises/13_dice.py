"""
9-13. Dice
Make a class Die with one attribute called sides, which has a default
value of 6.
"""

from random import randint

class Die():
    """Simple model of a die."""

    def __init__(self, sides=6):
        """Initialize the attribute."""
        self.sides = sides


# Write a method called roll_die() that prints a random number between 1
# and the number of sides the die has.
    def roll_die(self):
        """Prints a random number between 1 and the number of sides."""
        print(randint(1, self.sides))

# Make a 6-sided die and roll it 10 times.
d6 = Die()
print("-=-=-= d6 =-=-=-")
for roll in range(1, 11):
    d6.roll_die()

# Make a 10-sided die and a 20-sided die. Roll each die 10 times.
d10 = Die(10)
d20 = Die(20)
print("-=-=-= d10 =-=-=-")
for roll in range(1, 11):
    d10.roll_die()

print("-=-=-= d20 =-=-=-")
for roll in range(1, 11):
    d20.roll_die()
