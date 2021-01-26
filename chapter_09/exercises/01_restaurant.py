"""
9-1. Restaurant
Make a class called Restaurant. The __init__() method for Restaurant
should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces
of information, and a method called open_restaurant() that prints a
message indicating that the restaurant is open.
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


# Make an instance called restaurant from your class.
restaurant = Restaurant('Mc Donalds', 'Fast-food')

# Print the two attributes individually, and then call both methods.
restaurant.describe_restaurant()
restaurant.open_restaurant()
