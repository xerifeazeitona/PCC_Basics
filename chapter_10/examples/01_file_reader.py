"""
Open, read and print the contents of the file pi_digits.txt
"""
file_path = "pi_digits.txt"
with open(file_path) as file_object:
    contents = file_object.read()
print("\nPrinting entire file...")
print(contents.rstrip())

# You can use a for loop on the file object to examine each line from a 
# file, one at a time
print("\nPrinting line by line...")
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())

# If you want to retain access to a file’s contents outside the with
# block, you can store the file’s lines in a list inside the block and
# then work with that list
print("\nPrinting a list of lines from the file...")
with open(file_path) as file_object:
    # readlines() takes each line from the file and stores it in a list
    lines = file_object.readlines()

for line in lines:
    print(line, end="")
