# 4-12. More Loops
# All versions of foods.py in this section have avoided using for loops
# when printing to save space. Choose a version of foods.py, and write
# two for loops to print each list of foods.

my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

my_foods.append("ice cream")
print("My favorite foods are:")
for food in my_foods:
    print(f" - {food}")

friends_foods.append('cannoli')
print("\nMy friend's favorite foods are:")
for food in friends_foods:
    print(f" - {food}")
