# Simplest kind of if statement
age = 19

if age >= 18:
    print('You are old enough to vote!')
    print('Have you registered to vote yet?')

# expanding to if-else
age = 17

if age >= 18:
    print('You are old enough to vote!')
    print('Have you registered to vote yet?')
else:
    print('Sorry, you are too young to vote.')
    print('Please refgister to vote as soon as you turn 18!')

# the if-elif-else chain
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")

# multiple elif blocks
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
    
print(f"Your admission cost is ${price}.")