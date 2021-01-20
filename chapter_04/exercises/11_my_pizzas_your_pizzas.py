# 4-11. My Pizzas, Your Pizzas
# Start with your program from Exercise 4-1. 
pizzas = ['canadian', 'pepperoni', 'mozzarella']
for pizza in pizzas:
    print(pizza)

# Make a copy of the list of pizzas, and call it friend_pizzas. 
friends_pizzas = pizzas[:]

# Then, do the following: Add a new pizza to the original list.
pizzas.append('neopolitan')

# Add a different pizza to the list friend_pizzas.
friends_pizzas.append('meat lovers')

# Prove that you have two separate lists. Print the message "My favorite
# pizzas are:", and then use a for loop to print the first list. 
print("\nMy favorite pizzas are:")
for pizza in pizzas:
    print(f"- {pizza}")

# Print the message "My friend’s favorite pizzas are:", and then use a
# for loop to print the second list. Make sure each new pizza is stored
# in the appropriate list.
print("\nMy friends' favorite pizzas are:")
for pizza in friends_pizzas:
    print(f"- {pizza}")
