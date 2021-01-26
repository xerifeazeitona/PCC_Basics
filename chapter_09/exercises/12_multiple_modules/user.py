"""
9-12. Multiple Modules: Store the User class in one module.
"""

class User:
    """Simple representation of a user."""

    def __init__(self, first_name, last_name, username, sex, age):
        """Initialize the class attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.sex = sex
        self.age = age
        self.login_attempts = 0


    def describe_user(self):
        """Prints a summary of the user's information."""
        print(f"\nUsername: {self.username}")
        print(f"Full name: {self.first_name.title()} {self.last_name.title()}")
        print(f"Age: {self.age}")
        print(f"Sex: {self.sex}")


    def greet_user(self):
        """Prints a personalized greeting to the user."""
        print(f"\nHello, {self.first_name.title()}!")

