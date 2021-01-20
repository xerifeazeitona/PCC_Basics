# Python’s range() function makes it easy to generate a series of numbers
for value in range(1,5):
    print(value)

# You can also pass range() only one argument, and it will start the
# sequence of numbers at 0
print()
for value in range(5):
    print(value)

# If you want to make a list of numbers, you can convert the results of
# range() directly into a list using the list() function.
print()
numbers = list(range(1,6))
print(numbers)

# If you pass a third argument to range(), Python uses that value as a
# step size when generating numbers
print()
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# You can create almost any set of numbers you want to using the range()
# function. For example, consider how you might make a list of the first
# 10 square numbers
print()
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

# A list comprehension combines the for loop and the creation of new
# elements into one line, and automatically appends each new element
print()
squares = [value**2 for value in range(1, 11)]
print(squares)