"""
9-11. Imported Admin: Start with your work from Exercise 9-8.
Store the classes User, Privileges, and Admin in one module. 
"""

class Privileges():
    """Simple model of an administrator's privileges."""

    def __init__(self, privileges):
        """Initialize the class attribute."""
        self.privileges = privileges


    def show_privileges(self):
        """Lists the administrator's set of privileges."""
        for privilege in self.privileges:
            print(f"- {privilege}")


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


class Admin(User):
    """Model of a user that has extra privileges over regular users."""

    def __init__(self, first_name, last_name, username, sex, age, privileges):
        """
        Initialize parent attributes.
        Then initialize own attribute.
        """
        super().__init__(first_name, last_name, username, sex, age)
        self.privileges = Privileges(privileges)
