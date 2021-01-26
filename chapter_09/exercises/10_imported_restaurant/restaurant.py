"""
9-10. Imported Restaurant
Using your latest Restaurant class, store it in a module. 
"""

class Restaurant:
    """Crude representation of a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initializes the Restaurant class attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        """Prints the restaurant name and cuisine type."""
        print(f"\nRestaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")


    def open_restaurant(self):
        """Prints a message indicating that the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")


    def set_number_served(self, number):
        """Set the number of customers that have been served."""
        self.number_served = number


    def increment_number_served(self, number):
        """Increment the number of customers who’ve been served."""
        self.number_served += number
