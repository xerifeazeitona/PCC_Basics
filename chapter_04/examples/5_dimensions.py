# A tuple looks just like a list except you use parentheses instead of
# square brackets
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Tuples are immutable lists. 
# The code below will generate an error, if uncommented:
#dimensions[0] = 250

# If you want to define a tuple with one element, you need to include a
# trailing comma
my_tuple = (3,)

print()
# You can loop over all the values in a tuple using a for loop
for dimension in dimensions:
    print(dimension)

print()
# Although you can’t modify a tuple, you can assign a new value to a
# variable that represents a tuple
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("Modified dimensions:")
for dimension in dimensions:
    print(dimension)
