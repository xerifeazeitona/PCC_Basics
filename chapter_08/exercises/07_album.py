"""
8-7. Album
Write a function called make_album() that builds a dictionary describing
a music album. The function should take in an artist name and an album
title, and it should return a dictionary containing these two pieces of
information.
Use None to add an optional parameter to make_album() that allows you to
store the number of songs on an album. If the calling line includes a
value for the number of songs, add that value to the album’s dictionary.
"""
def make_album(artist_name, album_title, songs=None):
    """Returns a dictionary describing a music album."""
    album = {'artist': artist_name, 'title': album_title}
    if songs:
        album['songs'] = songs
    return album

# Use the function to make three dictionaries representing different
# albums.
album_0 = make_album('pink floyd', 'dark side of the moon')
album_1 = make_album('dream theater', 'awake')
album_2 = make_album('madonna', 'mdna')

# Print each return value to show that the dictionaries are storing the
# album information correctly.
albums = [album_0, album_1, album_2]
for a in albums:
    print(a)

# Make at least one new function call that includes the number of songs
# on an album.
u2 = make_album('u2', 'joshua tree', 12)
print(u2)
