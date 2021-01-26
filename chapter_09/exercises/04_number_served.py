"""
9-4. Number Served
Start with your program from Exercise 9-1.
"""
class Restaurant:
    """Crude representation of a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initializes the Restaurant class attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
# Add an attribute called number_served with a default value of 0.
        self.number_served = 0


    def describe_restaurant(self):
        """Prints the restaurant name and cuisine type."""
        print(f"\nRestaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")


    def open_restaurant(self):
        """Prints a message indicating that the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")


# Add a method called set_number_served() that lets you set the number
# of customers that have been served. 
    def set_number_served(self, number):
        """Set the number of customers that have been served."""
        self.number_served = number


# Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served. 
    def increment_number_served(self, number):
        """Increment the number of customers who’ve been served."""
        self.number_served += number


# Create an instance called restaurant from this class.
restaurant = Restaurant('Mc Donalds', 'Fast-food')
restaurant.describe_restaurant()
restaurant.open_restaurant()

# Print the number of customers the restaurant has served, and then
# change this value and print it again.
print(f"This restaurant has served {restaurant.number_served} customers.")

# Call the method set_number_served with a new number and print the
# value again.
restaurant.set_number_served(10)
print(f"This restaurant has now served {restaurant.number_served} customers.")

# Call the method increment_number_served() with any number you like
# that could represent how many customers were served in, say, a day of
# business.
restaurant.increment_number_served(5)
print(f"This restaurant has now served {restaurant.number_served} customers.")
