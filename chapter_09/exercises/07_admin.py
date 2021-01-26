"""
9-7. Admin
An administrator is a special kind of user. Write a class called Admin
that inherits from the User class you wrote in Exercise 9-3 or Exercise
9-5.
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


class Admin(User):
    """Model of a user that has extra privileges over regular users."""

    def __init__(self, first_name, last_name, username, sex, age, privileges):
        """
        Initialize parent attributes.
        Then initialize own attribute.
        """
        super().__init__(first_name, last_name, username, sex, age)
# Add an attribute, privileges, that stores a list of strings like "can
# add post", "can delete post", "can ban user", and so on.
        self.privileges = privileges


# Write a method called show_privileges() that lists the administrator’s
# set of privileges.
    def show_privileges(self):
        """Lists the administrator's set of privileges."""
        for privilege in self.privileges:
            print(f"- {privilege}")


# Create an instance of Admin, and call your method.
administrator_privileges = [
    'can add post',
    'can delete post',
    'can ban user',
    'and so on :)'
]
administrator = Admin(
    'carla',
    'banks',
    'beefyboi',
    'F',
    7,
    administrator_privileges
    )
administrator.show_privileges()
