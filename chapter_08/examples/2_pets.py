# Positional arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet("hamster", "harry")

# You can call a function as many times as needed
describe_pet("parrot", "polly")
describe_pet("dog", "monty")
describe_pet("cat", "mr. whiskers")

# Order Matters in Positional Arguments!
describe_pet("harry", "hamster")

# Keyword arguments free you from having to worry about correctly
# ordering your arguments in the function call, and they clarify the
# role of each value in the function call
describe_pet(pet_name="harry", animal_type="hamster")
describe_pet(animal_type="hamster", pet_name="harry")

# Default values
def describe_pet_v2(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet_v2("monty")

# Equivalent Function Calls (all are valid uses and also
# return the same results)
describe_pet_v2("monty")
describe_pet_v2(pet_name="monty")
describe_pet_v2("monty", "dog")
describe_pet_v2(pet_name="monty", animal_type="dog")
describe_pet_v2(animal_type="dog", pet_name="monty")
