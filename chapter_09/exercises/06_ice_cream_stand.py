"""
9-6. Ice Cream Stand
An ice cream stand is a specific kind of restaurant. Write a class
called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 or Exercise 9-4. Either version of the class will work;
just pick the one you like better.
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


class IceCreamStand(Restaurant):
    """Simple model of a specific type of restaurant."""

    def __init__(self, restaurant_name, flavors):
        super().__init__(restaurant_name, 'Ice Cream')
# Add an attribute called flavors that stores a list of ice cream
#  flavors.
        self.flavors = flavors


# Write a method that displays the flavors.
    def display_flavors(self):
        """Print the available flavors."""
        for flavor in self.flavors:
            print(f"- {flavor}")

# Create an instance of IceCreamStand, and call the disply_flavors()
# method.
available_flavors = ['chocolate', 'mint', 'rocky roads']
stand = IceCreamStand('Lickety Slurp', available_flavors)

stand.display_flavors()
