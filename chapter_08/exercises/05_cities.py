"""
8-5. Cities
Write a function called describe_city() that accepts the name of a city
and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland. Give the parameter for the country a default
value.
"""
def describe_city(city, country='canada'):
    """Prints a simple sentence telling in which country the city is in."""
    print(f"{city.title()} is in {country.title()}.")

# Call your function for three different cities, at least one of which
# is not in the default country.
describe_city('toronto')
describe_city('vancouver')
describe_city('Reykjavik', 'iceland')
