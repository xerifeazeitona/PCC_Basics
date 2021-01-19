# Python’s sort() method makes it relatively easy to sort a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# You can also sort this list in reverse alphabetical order by passing
# the argument reverse=True to the sort() method
cars.sort(reverse=True)
print(cars)

# To maintain the original order of a list but present it in a sorted
# order, you can use the sorted() function:
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

# To reverse the original order of a list, you can use the reverse()
# method:
print("\n")
print(cars)
cars.reverse()
print(cars)

# You can quickly find the length of a list by using the len() function
message = f"\nThe cars list has a length of {len(cars)}"
print(message)