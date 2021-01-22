# 7-8. Deli
# Make a list called sandwich_orders and fill it with the names of
# various sandwiches.
sandwich_orders = ['hamburger', 'cheeseburger', 'grilled cheese']

# Then make an empty list called finished_sandwiches.
finished_sandwiches = []

# Loop through the list of sandwich orders and print a message for each
# order, such as I made your tuna sandwich. As each sandwich is made,
# move it to the list of finished sandwiches. 
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich}.")
    finished_sandwiches.append(sandwich)

# After all the sandwiches have been made, print a message listing each
# sandwich that was made.
print("\n Sandwiches that were made:")
for finished_sandwich in finished_sandwiches:
    print(f"- {finished_sandwich}")
    