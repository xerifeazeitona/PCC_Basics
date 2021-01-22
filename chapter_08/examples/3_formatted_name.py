# Returning a simple value
def get_formatted_name_v1(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name_v1('jimi', 'hendrix')
print(musician)

# You can use default values to make an argument optional
def get_formatted_name_v2(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name_v2('jimi', 'hendrix')
print(musician)
musician = get_formatted_name_v2('john', 'hooker', 'lee')
print(musician)

