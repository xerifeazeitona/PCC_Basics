"""
The Python standard library is a set of modules included with every
Python installation.
You can use any function or class in the standard library by including a
simple import statement at the top of your file. Let’s look at one
module, random , which can be useful in modeling many real-world
situations.
"""

from random import randint, choice

# The randint() function takes two integer arguments and returns a
# randomly selected integer between (and including) those numbers.
dice_roll = randint(1, 6)
print(dice_roll)

# The choice() function takes in a list or tuple and returns a randomly
# chosen element.
players = ['charles', 'martine', 'michael', 'florence', 'eli']
first_up = choice(players)
print(first_up)
