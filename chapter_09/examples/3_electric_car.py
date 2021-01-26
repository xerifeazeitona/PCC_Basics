"""
If the class you’re writing is a specialized version of another class
you wrote, you can use inheritance. When one class inherits from
another, it takes on the attributes and methods of the first class.
"""
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


    def fill_gas_tank(self):
        """Fill the gas tank."""
        print("This car's gas tank is now full.")

# When modeling something from the real world in code, you may find that
# you’re adding more and more detail to a class. You’ll find that you
# have a growing list of attributes and methods and that your files are
# becoming lengthy. In these situations, you might recognize that part
# of one class can be written as a separate class. You can break your
#  large class into smaller classes that work together.
class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size


    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            battery_range = 260
        elif self.battery_size == 100:
            battery_range = 315

        print(f"This car can go about {battery_range} miles on a full charge.")


# Once you have a child class that inherits from a parent class, you can
# add any new attributes and methods necessary to differentiate the
# child class from the parent class.
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initializes attributes o the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


    # You can override any method from the parent class that doesn’t fit
    # what you’re trying to model with the child class. To do this, you
    # define a method in the child class with the same name as the
    # method you want to override in the parent class.
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car's doesn't have a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.fill_gas_tank()
