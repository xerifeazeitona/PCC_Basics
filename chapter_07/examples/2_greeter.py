# Each time you use the input() function, you should include a clear,
# easy-to-follow prompt that tells the user exactly what kind of
# information you’re looking for
name = input("Please enter your name: ")
print(f"Hello, {name}!")

# You can assign your prompt to a variable and pass that variable to the
# input() function
prompt = "If you tell us your first name, we can personalize the messages " \
    "you see."
prompt += "\nWhat's your first name? "

name= input(prompt)
print(f"\nHello, {name}!")
