# 5-2. More Conditional Tests
# You don’t have to limit the number of tests you create to ten. If you
# want to try more comparisons, write more tests. Have at least one True
# and one False result for each of the following:

# Tests for equality and inequality with strings
color = 'Blue'
print(color == 'Blue')
print(color != 'Red')

# Tests using the lower() method
print(color == 'blue')
print(color.lower() == 'blue')

# Numerical tests involving equality and inequality, greater than and
# less than, greater than or equal to, and less than or equal to
number = 7
print(number == 7)
print(number != 10)
print(number > 5)
print(number < 10)
print(number <= 8)
print(number >= 7)

# Tests using the and keyword and the or keyword
print((color.lower() == 'blue') and (number == 7))
print((color == 'blue') or (number >= 5))

# Test whether an item is in a list
odd_numbers = [value for value in range(1, 11, 2)]
print(number in odd_numbers)

# Test whether an item is not in a list
print(number not in odd_numbers)