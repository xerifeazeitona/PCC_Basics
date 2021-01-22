# Defining a Function

def greet_user():
    """Display a simple greeting"""
    print("Hello!")

greet_user()

# Modified slightly, greet_user can also greet by name
def greet_user_by_name(username):
    """Display a simple greeting"""
    print(f"Hello, {username.title()}!")

greet_user_by_name("larry")

# You can use a function with a while loop
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

prompt = "\nPlease tell me your name:"
prompt += "\n(Enter 'q' to quit) "
while True:
    print(prompt)

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"Hello, {formatted_name}!")
    