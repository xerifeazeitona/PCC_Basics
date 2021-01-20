# 5-1. Conditional Tests
# Write a series of conditional tests. Print a  statement describing
# each test and your prediction for the results of each test. Your code
# should look something like this:
#
#car = 'subaru'
#print("Is car == 'subaru'? I predict True.")
#print(car == 'subaru')
#print("\nIs car == 'audi'? I predict False.")
#print(car == 'audi')
#
# Look closely at your results, and make sure you understand why each
# line evaluates to True or False.
fruit = 'kiwi'
print('Is fruit a kiwi? I predict True.')
print(fruit == 'kiwi')

print('Is fruit a blueberry? I predict False.')
print(fruit == 'blueberry')
print()

# Create at least ten tests. Have at least five tests evaluate to True
# and another five tests evaluate to False.
numbers = [value for value in range(1, 11)]
for number in numbers:
    print(number % 2 == 0)