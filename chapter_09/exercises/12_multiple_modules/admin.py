"""
Store the Privileges and Admin classes in a separate module.
"""

from user import User

class Privileges():
    """Simple model of an administrator's privileges."""

    def __init__(self, privileges):
        """Initialize the class attribute."""
        self.privileges = privileges


    def show_privileges(self):
        """Lists the administrator's set of privileges."""
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    """Model of a user that has extra privileges over regular users."""

    def __init__(self, first_name, last_name, username, sex, age, privileges):
        """
        Initialize parent attributes.
        Then initialize own attribute.
        """
        super().__init__(first_name, last_name, username, sex, age)
        self.privileges = Privileges(privileges)
