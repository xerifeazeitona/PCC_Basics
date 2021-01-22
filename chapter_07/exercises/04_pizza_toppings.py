# 7-4. Pizza Toppings
# Write a loop that prompts the user to enter a series of pizza toppings
# until they enter a 'quit' value. As they enter each topping, print a
# message saying you’ll add that topping to their pizza.
toppings = []

prompt = "\nEnter a topping you would like to add to your pizza:"
prompt += "\n(Enter 'q' when you're done) "

while True:
    topping = input(prompt)

    if topping == 'q':
        break
    else:
        print(f"Adding {topping} to your pizza.")
        toppings.append(topping)

print("\nYour pizza will have the following toppings:")
for top in toppings:
    print(f"- {top}")
