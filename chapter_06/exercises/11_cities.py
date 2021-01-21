# 6-11. Cities
# Make a dictionary called cities. Use the names of three cities as keys
# in your dictionary. Create a dictionary of information about each city
# and include the country that the city is in, its approximate
# population, and one fact about that city.
# The keys for each city’s dictionary should be something like country,
# population, and fact.
cities = {
    'toronto': {
        'country': 'canada',
        'population': '10',
        'fact': 'nice place',
    },
    'buenos aires': {
        'country': 'argentina',
        'population': '5',
        'fact': 'down south',
    },
    'tokyo': {
        'country': 'japan',
        'population': '8',
        'fact': 'big robots',
    },
}

# Print the name of each city and all of the information you have stored
# about it.
for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    for key, value in info.items():
        print(f"{key.title()}: {value}")
