# Adding tab
print("Python")
print("\tPython")

# Adding new line
print("\nLanguages:\nPython\nC\nJavaScript")

# Tabs and new lines
print("\nLanguages:\n\tPython\n\tC\n\tJavaScript")

favorite_language = ' Python '
print(f"\nOriginal: '{favorite_language}'")
# Stripping whitespace to the right
print(f"  rstrip: '{favorite_language.rstrip()}'")

# Stripping whitespace to the left
print(f"  lstrip: '{favorite_language.lstrip()}'")

# Stripping whitespace from both sides at the same time
print(f"   strip: '{favorite_language.strip()}'")