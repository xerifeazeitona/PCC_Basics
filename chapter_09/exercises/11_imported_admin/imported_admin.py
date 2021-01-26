"""
Create a separate file, make an Admin instance, and call
show_privileges() to show that everything is working correctly.
"""

from user import Admin as adm

administrator_privileges = [
    'can add post',
    'can delete post',
    'can ban user',
    'and so on :)'
]
administrator = adm(
    'carla',
    'banks',
    'beefyboi',
    'F',
    7,
    administrator_privileges
    )
administrator.privileges.show_privileges()
