"""
Exceptions are handled with try-except blocks. When you use try-except
blocks, your programs will continue running even if things start to go
wrong. Instead of tracebacks, which can be confusing for users to read,
users will see friendly error messages that you write.
"""

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    # Any code that depends on the try block executing successfully goes
    # in the else block
    else:
        print(answer)
