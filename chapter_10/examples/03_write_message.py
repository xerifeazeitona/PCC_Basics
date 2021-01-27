"""
To write text to a file, you need to call open() with a second argument
telling Python that you want to write to the file.
"""
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# If you want to add content instead of overwriting existing content,
# you can open the file in append mode
with open(filename, 'a') as file_object:
    file_object.write("I also finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
