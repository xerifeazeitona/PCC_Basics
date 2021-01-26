"""
We can now import from each module and create any kind of car we need
"""

from car import Car
# aliases can be quite helpful when using modules to organize your
# projects’ code. You can use aliases when importing classes as well.
from electric_car import ElectricCar as EC

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = EC('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
