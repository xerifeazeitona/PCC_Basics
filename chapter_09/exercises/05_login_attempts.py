"""
9-5. Login Attempts
Add an attribute called login_attempts to your User class from
Exercise 9-3.
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


# Write a method called increment_login_attempts() that increments the
# value of login_attempts by 1.
    def increment_login_attempts(self):
        """Increments the value of login_attempts by 1."""
        self.login_attempts += 1


# Write another method called reset_login_attempts() that resets the
# value of login_attempts to 0.
    def reset_login_attempts(self):
        """Resets the value of login_attempts to 0."""
        self.login_attempts = 0


# Make an instance of the User class and call increment_login_attempts()
# several times.
new_user = User('kelly', 'smith', 'sassygal69', 'F', 83)
new_user.describe_user()

new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()

# Print the value of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts().
print(f"{new_user.username} has attempted to login {new_user.login_attempts}" \
    " times so far.")
new_user.reset_login_attempts()

# Print login_attempts again to make sure it was reset to 0.
print(f"{new_user.username} has attempted to login {new_user.login_attempts}" \
    " times so far.")
