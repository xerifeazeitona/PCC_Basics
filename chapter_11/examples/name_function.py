"""
The function get_formatted_name() combines the first and last name with
a space in between to complete a full name, and then capitalizes and
returns the full name.
"""
def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
