"""
8-8. User Albums
Start with your program from Exercise 8-7.
Write a while loop that allows users to enter an album’s artist and
title. Once you have that information, call make_album() with the user’s
input and print the dictionary that’s created. Be sure to include a quit
value in the while loop.
"""
def make_album(artist_name, album_title, songs=None):
    """Returns a dictionary describing a music album."""
    album = {'artist': artist_name, 'title': album_title}
    if songs:
        album['songs'] = songs
    return album

prompt = "\nPlease tell me the album information:"
prompt += "\n(Enter 'q' to quit) "
while True:
    print(prompt)

    a_name = input("Artist name: ")
    if a_name == 'q':
        break

    a_title = input("Album title: ")
    if a_title == 'q':
        break

    a_songs = input("Number of songs: ")
    if a_songs == 'q':
        break

    alb = make_album(a_name, a_title, a_songs)
    print(alb)
    