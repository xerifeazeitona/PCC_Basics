"""
11-3. Employee
Write a test case for Employee. Write two test methods,
test_give_default_raise() and test_give_custom_raise().
Use the setUp() method so you don’t have to create a new employee
instance in each test method. Run your test case, and make sure both
tests pass.
"""

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee."""

    def setUp(self):
        """Create an Employee for use in tests."""
        self.employee = Employee('john', 'doe', 50000)

    def give_raise_test(self, amount=5000):
        """Test salary increase."""
        old_salary = self.employee.annual_salary
        self.employee.give_raise(amount)
        self.assertEqual(
            int(self.employee.annual_salary),
            int(old_salary) + int(amount)
            )

    def test_give_default_raise(self):
        """Test salary increase with the default value."""
        self.give_raise_test()

    def test_give_custom_raise(self):
        """Test salary increase with a custom value."""
        self.give_raise_test(10000)

if __name__ == "__main__":
    unittest.main()
