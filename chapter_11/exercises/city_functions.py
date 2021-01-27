"""
11-1. City, Country
Write a function that accepts two parameters: a city name and a country
name. The function should return a single string of the form City,
Country, such as Santiago, Chile. Store the function in a module called
city_functions.py.

11-2. Population
Modify your function so it requires a third parameter, population. It
should now return a single string of the form City, Country – population
xxx, such as Santiago, Chile – population 5000000. Run test_cities.py
again. Make sure test_city_country() fails this time.
Modify the function so the population parameter is optional.
Run test_cities.py again, and make sure test_city_country() passes
again.
"""

def get_location(city, country, population=''):
    """Return a neatly formatted location."""
    if population:
        location = f"{city}, {country} - population {population}"
    else:
        location = f"{city}, {country}"
    return location.title()
