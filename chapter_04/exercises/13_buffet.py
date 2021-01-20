# 4-13. Buffet
# A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.
menu = ('eggs', 'bacon', 'hash browns', 'pork sausage', 'turkey links')

# Use a for loop to print each food the restaurant offers.
print("Breakfast Menu")
for food in menu:
    print(f" - {food}")

# Try to modify one of the items, and make sure that Python rejects the
# change. (uncomment and run to see the error)
#menu[2] = 'waffles'

# The restaurant changes its menu, replacing two of the items with
# different foods. Add a line that rewrites the tuple, and then use a 
# for loop to print each of the items on the revised menu.
menu = ('eggs', 'oatmeal', 'hash browns', 'waffles', 'turkey links')

print("New (pork-free) Breakfast Menu")
for food in menu:
    print(f" - {food}")
