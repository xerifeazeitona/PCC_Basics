"""
11-3. Employee
Write a class called Employee. The __init__() method should take in a
first name, a last name, and an annual salary, and store each of these
as attributes.
Write a method called give_raise() that adds $5,000 to the annual salary
by default but also accepts a different raise amount.
"""

class Employee:
    """Simple model of an Employee."""

    def __init__(self, first, last, salary):
        """Initialize the class attributes."""
        self.first_name = first
        self.last_name = last
        self.annual_salary = salary

    def give_raise(self, amount=5000):
        """Adds the provided amount to the annual salary."""
        self.annual_salary += amount
        