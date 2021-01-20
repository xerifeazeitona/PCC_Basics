# When you want to do the same action with every item in a list, you can
# use Python’s for loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

print()
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

print()
# You can also write as many lines of code as you like in the for loop
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

# Any lines of code after the for loop that are not indented are executed once without repetition
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you everyone, That was a great magic show!")