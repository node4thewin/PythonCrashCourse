# Album

# Write a function called 'make_album()' that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the dictionaries are storing the information correctly.

# Use 'None' to add an optional parameter to 'make_album()' that allows you to store the number of songs on an album. If the calling line includes a value for the number of songs, add that value to the album's dictionary. Make at least one new function call that includes the number of songs on an album.

def make_album(name, title, songs=None):
  """Take artist name, album title, and return a dictionary of contents"""
  album = {'name': name, 'title': title}
  if songs:
    album['songs'] = songs    
  return album

record = make_album('beyonce', 'lemonade')
print(record)

record = make_album('red hot chili peppers', 'californication')
print(record)

record = make_album('ariana grande', 'thank u, next')
print(record)

record = make_album('blackbear', 'everything means nothing', '12')
print(record)

