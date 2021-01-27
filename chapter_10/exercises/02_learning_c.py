"""
10-2. Learning C
You can use the replace() method to replace any word in a string with a
different word.
Read in each line from the file you just created, learning_python.txt,
and replace the word Python with the name of another language, such as
C. Print each modified line to the screen.
"""
file_path = "learning_python.txt"

with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip().replace('Python', 'C'))
