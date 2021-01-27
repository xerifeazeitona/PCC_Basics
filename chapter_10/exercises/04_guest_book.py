"""
10-4. Guest Book
Write a while loop that prompts users for their name. When they enter
their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt. Make sure each entry
appears on a new line in the file.
"""
prompt = "Enter your name to be immortalized"
prompt += "\n(Enter 'q' to quit): "

with open('guest_book.txt', 'w') as file_object:
    while True:
        name = input(prompt)
        if name == 'q':
            break
        else:
            print(f"Hello {name.title()}! " \
                "Your visit has been recorded into our guest book.")
            file_object.write(name + "\n")
