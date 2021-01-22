"""
8-12. Sandwiches
Write a function that accepts a list of items a person wants on a
sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of
the sandwich that’s being ordered.
"""
def print_sandwiches(*sandwiches):
    """Prints a summary of the sandwiches being ordered"""
    print("\nSandwiches in this order:")
    for sandwich in sandwiches:
        print(f"- {sandwich}")

# Call the function three times, using a different number of arguments
# each time.
print_sandwiches('pastrami')
print_sandwiches('cheeseburger', 'hamburger', 'grilled chicken')
print_sandwiches('tuna', 'grilled cheese')
