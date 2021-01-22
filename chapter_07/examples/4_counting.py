# You can use a while loop to count up through a series of numbers
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# you can use the continue statement to return to the beginning of the
# loop based on the result of a conditional test
print("\nHere are the odd numbers between 0 and 10:")
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)
