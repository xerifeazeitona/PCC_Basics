"""
8-6. City Names
Write a function called city_country() that takes in the name of a city
and its country. The function should return a string formatted like
this:
"Santiago, Chile"
"""
def city_country(city, country):
    """Returns a formatted string with the city name and the country"""
    return f'"{city.title()}, {country.title()}"'

# Call your function with at least three city-country pairs, and print
# the values that are returned.
print(city_country('santiago','chile'))
print(city_country('toronto','canada'))
print(city_country('lisbon','portugal'))
