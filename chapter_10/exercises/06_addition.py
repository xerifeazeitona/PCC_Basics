"""
10-6. Addition
One common problem when prompting for numerical input occurs when people
provide text instead of numbers. When you try to convert the input to an
int, you’ll get a ValueError. 
Write a program that prompts for two numbers.
Add them together and print the result.
Catch the ValueError if either input value is not a number, and print a
friendly error message.
Test your program by entering two numbers and then by entering some text
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

print("\nEnter two numbers and I'll add them for you.")
first_number = input("First number: ")
second_number = input("Second number: ")
sum_numbers(first_number, second_number)
