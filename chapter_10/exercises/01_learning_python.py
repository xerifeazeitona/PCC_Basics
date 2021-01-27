"""
10-1. Learning Python
Open a blank file in your text editor and write a few lines summarizing
what you’ve learned about Python so far. Start each line with the phrase
"In Python you can. . . ."
Save the file as learning_python.txt in the same directory as your
exercises from this chapter.

Write a program that reads the file and prints what you wrote three
times.
Print the contents:
- once by reading in the entire file
- once by looping over the file object
- once by storing the lines in a list and then working with them outside
the with block.
"""
file_path = "learning_python.txt"

print("\nReading the entire file...")
with open(file_path) as file_object:
    print(file_object.read().rstrip())

print("\nLooping over the file object...")
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())

print("\nOutside the with block...")
with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
