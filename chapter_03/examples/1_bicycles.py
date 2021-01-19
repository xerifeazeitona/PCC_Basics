bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# If you ask to print a list, Python returns its representation of the list
print(bicycles)

# To access an element in a list, write the name of the list followed by the
# index of the item enclosed in square brackets
print(bicycles[0])

# You can also use the string methods on any element in the list
print(bicycles[0].title())

# By asking for the item at index -1, Python always returns the last item
print(bicycles[-1])

# You can use f-strings to create a message based on a value from a list
messsage = f"My first bicycle was a {bicycles[0].title()}."
print(messsage)