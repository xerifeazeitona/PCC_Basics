"""
9-3. Users
Make a class called User. Create two attributes called first_name and
last_name, and then create several other attributes that are typically
stored in a user profile.
Make a method called describe_user() that prints a summary of the user’s
information. 
Make another method called greet_user() that prints a personalized
greeting to the user.
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


    def describe_user(self):
        """Prints a summary of the user's information."""
        print(f"\nUsername: {self.username}")
        print(f"Full name: {self.first_name.title()} {self.last_name.title()}")
        print(f"Age: {self.age}")
        print(f"Sex: {self.sex}")


    def greet_user(self):
        """Prints a personalized greeting to the user."""
        print(f"\nHello, {self.first_name.title()}!")


# Create several instances representing different users, and call both
# methods for each user.
user_0 = User('john', 'doe', 'johnny', 'M', 24)
user_1 = User('claire', 'stevens', 'cstevens', 'F', 48)
user_2 = User('mary', 'sullivan', 'mary_s', 'F', 32)
user_3 = User('larry', 'jules', 'lammerdude', 'M', 33)

user_0.describe_user()
user_0.greet_user()
user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user()
user_3.describe_user()
user_3.greet_user()
