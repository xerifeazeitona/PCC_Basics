"""
The json module allows you to dump simple Python data structures into a
file and load the data from that file the next time the program runs.
You can also use json to share data between different Python programs.
"""

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)
