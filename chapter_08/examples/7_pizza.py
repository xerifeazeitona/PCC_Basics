# Passing an Arbitrary Number of Arguments
# The function in the following example has one parameter, *toppings,
# but this parameter collects as many arguments as the calling line
# provides:
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green pepper', 'extra cheese')

# If you want a function to accept several different kinds of arguments,
# the parameter that accepts an arbitrary number of arguments must be
# placed last in the function definition.
def make_pizza_v2(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza_v2(16, 'pepperoni')
make_pizza_v2(12, 'mushrooms', 'green peppers', 'extra cheese')
