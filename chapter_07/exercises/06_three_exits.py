# 7-6. Three Exits
# Write different versions of either Exercise 7-4 or Exercise 7-5 that
# do each of the following at least once:
prompt = "\nEnter a topping you would like to add to your pizza:"
prompt += "\n(Enter 'q' when you're done) "

# Use a conditional test in the while statement to stop the loop.
topping = ""
while topping != 'q':
    topping = input(prompt)

    if topping != 'q':
        print(f"Adding {topping} to your pizza.")

# Use an active variable to control how long the loop runs.
active = True
while active:
    topping = input(prompt)

    if topping == 'q':
        active = False
    else:
        print(f"Adding {topping} to your pizza.")

# Use a break statement to exit the loop when the user enters a 'quit'
# value.
while True:
    topping = input(prompt)

    if topping == 'q':
        break
    else:
        print(f"Adding {topping} to your pizza.")
