# 6-5. Rivers
# Make a dictionary containing three major rivers and the country each
# river runs through. One key-value pair might be 'nile': 'egypt'.
major_rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china',
    }

# Use a loop to print a sentence about each river, such as "The Nile 
# runs through Egypt".
for river, country in major_rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print()
# Use a loop to print the name of each river included in the dictionary.
for river in major_rivers:
    print(river.title())

print()
# Use a loop to print the name of each country included in the
# dictionary.
for country in major_rivers.values():
    print(country.title())
    