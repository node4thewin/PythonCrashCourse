# 8-8 User Albums

# Start with your program from Exercise 8-7. Write a 'while' loop that allows users to enter an album's artist and title. Once you have that information, call 'make_album()' with the user's input and print the dictionary that's created. Be sure to include a 'quit value' in the 'while' loop.

def make_album(artist, title, songs=None):
  """Display album/artist with user input and quit value."""
  album = {'artist': artist.title(), 'title': title.title()}
  if songs:
    album['songs'] = songs    
  return album

while True:
  print("\nPlease give me an Artist and one of their Albums: ")
  print("(If you'd like to quit at any time enter 'q')\n")

  artist = input("Artist: ")
  if artist == 'q':
    break

  title = input("Title: ")
  if title == 'q':
    break

  formatted_album = make_album(artist, title)
  print(formatted_album)