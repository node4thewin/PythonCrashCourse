# 10-12 Favorite Number Remembered

# Combine the two programs from Exercise 10-11 into one file. If the number is already stored, report the favorite number to the user. If not, prompt for the user's favorite number and store it in a file. Run the program twice to see that it works.

import json

def store_favorite_number():
  """Store user's favorite number."""
  filename = 'favorite_number.json'
  fav_num = input("Enter your favorite number: ")

  with open(filename, 'w') as f:
    json.dump(fav_num, f)
    return fav_num

def load_favorite_number():
  """Read user's favorite number."""
  try:
    filename = 'favorite_number.json'
    with open(filename) as f:
      fav_num = json.load(f)
  except FileNotFoundError:
    return None # this returns False
  else:
    return fav_num

def favorite_number():
  favorite_number = load_favorite_number()
  if favorite_number: # this needs True, so None would make it stop
    print(f"We found it! Your favorite number is {favorite_number}.")
  else:
    favorite_number = store_favorite_number()
    print("We'll remember your favorite number next time!")

favorite_number()
