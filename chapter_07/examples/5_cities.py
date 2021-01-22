# To exit a while loop immediately without running any remaining code in
# the loop, use the break statement
prompt = "\nEnter the name of a city you have visited:"
prompt += "\n(Enter 'q' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'q':
        break
    else:
        print(f"I'd love to go to {city.title()}")
