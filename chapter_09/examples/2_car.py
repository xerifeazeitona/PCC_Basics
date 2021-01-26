# When an instance is created, attributes can be defined without being
# passed in as parameters. These attributes can be defined in the
# __init__() method, where they are assigned a default value.
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")


    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles < 0:
            print("You can't roll back an odometer!")
        else:
            self.odometer_reading += miles


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# The simplest way to modify the value of an attribute is to access the
# attribute directly through an instance
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# It can be helpful to have methods that update certain attributes for
# you, especially when there's logic involving the update procedure.
# Instead of accessing the attribute directly, you pass the new value to
# a method that handles the updating internally.
my_new_car.update_odometer(32)
my_new_car.read_odometer()
my_new_car.update_odometer(10)

my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
