"""
10-7. Addition Calculator
Wrap your code from Exercise 10-6 in a while loop so the user can
continue entering numbers even if they make a mistake and enter text
instead of a number.
"""
def sum_numbers(first, second):
    """Sum two numbers and display the result."""
    try:
        answer = int(first) + int(second)
    except ValueError:
        print("What are you doing???")
    else:
        print(f"The sum of {first} and {second} is {answer}.")


print("Give me two numbers, and I'll sum them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    sum_numbers(first_number, second_number)
