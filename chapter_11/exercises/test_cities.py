"""
11-1. City, Country
Create a file called test_cities.py that tests the function you just
wrote (remember that you need to import unittest and the function you
want to test).
Write a method called test_city_country() to verify that calling your
function with values such as 'santiago' and 'chile' results in the
correct string.
Run test_cities.py, and make sure test_city_country() passes.

11-2. Population
Write a second test called test_city_country_population() that verifies
you can call your function with the values 'santiago' , 'chile' , and
'population=5000000'. Run test_cities.py again, and make sure this new
test passes.
"""

import unittest
from city_functions import get_location

class LocationsTestCase(unittest.TestCase):
    """Test for 'city_functions.py'."""

    def test_city_country(self):
        """Do locations like Santiago, Chile work?"""
        location = get_location('santiago', 'chile')
        self.assertEqual(location, 'Santiago, Chile')

    def test_city_country_population(self):
        """
        Do locations like Santiago, Chile - population 5000000 work?
        """
        location = get_location('santiago', 'chile', 5000000)
        self.assertEqual(location, 'Santiago, Chile - Population 5000000')

if __name__ == "__main__":
    unittest.main()
