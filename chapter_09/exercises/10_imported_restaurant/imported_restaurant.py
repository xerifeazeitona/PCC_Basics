"""
Make a separate file that imports Restaurant.
Make a Restaurant instance, and call one of Restaurant’s methods to show
that the import statement is working properly.
"""

from restaurant import Restaurant as rt

my_restaurant = rt('le chevallier', 'french')
my_restaurant.describe_restaurant()
