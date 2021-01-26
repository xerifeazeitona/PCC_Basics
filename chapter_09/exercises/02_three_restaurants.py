"""
9-2. Three Restaurants
Start with your class from Exercise 9-1.
"""
class Restaurant:
    """Crude representation of a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initializes the Restaurant class attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        """Prints the restaurant name and cuisine type."""
        print(f"\nRestaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")


    def open_restaurant(self):
        """Prints a message indicating that the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")


# Create three different instances from the class, and call 
# describe_restaurant() for each instance.
restaurant_0 = Restaurant('Mc Donalds', 'Fast-Food')
restaurant_1 = Restaurant('Red Lobster', 'Seafood')
restaurant_2 = Restaurant('Olive Garden', 'Italian')

restaurant_0.describe_restaurant()
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
