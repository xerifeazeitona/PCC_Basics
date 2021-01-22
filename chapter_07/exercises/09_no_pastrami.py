# 7-9. No Pastrami
# Using the list sandwich_orders from Exercise 7-8, make sure the
# sandwich 'pastrami' appears in the list at least three times.
sandwich_orders = ['pastrami', 'hamburger', 'pastrami', 'cheeseburger',
'pastrami', 'grilled cheese']

# Add code near the beginning of your program to print a message saying
# the deli has run out of pastrami,
print("\nThe Deli has run out of pastrami.")

# and then use a while loop to remove all occurrences of 'pastrami'
# from sandwich_orders.
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Make sure no pastrami sandwiches end up in finished_sandwiches.
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich}.")
    finished_sandwiches.append(sandwich)

print("\n Sandwiches that were made:")
for finished_sandwich in finished_sandwiches:
    print(f"- {finished_sandwich}")
