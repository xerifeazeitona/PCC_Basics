"""
After you’ve read a file into memory, you can do whatever you want with
that data.
"""

# You can build a single string containing all the text in the file
file_path = "/home/korporal/labs/PCC_Basics/chapter_10/examples/pi_digits.txt"
with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# Python has no inherent limit to how much data you can work with; you
# can work with as much data as your system’s memory can handle
file_path = "pi_million_digits.txt"
with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

# Once you’ve read from a file, you can analyze its contents in just about any
# way you can imagine. As another example, we can find out if someone’s
# birthday appears anywhere in the first million digits of pi
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
