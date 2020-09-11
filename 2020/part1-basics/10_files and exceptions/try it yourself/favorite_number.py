# 10-11 Favorite Number

# Write a program that promps for the user's favorite number. Use json.dump() to store this number in a file. Write a separate program that reads in this value and prints the message, "I know your favorite number! It's _____."

import json

fav_num = input("What's your favorite number? ")

filename = 'fav_num.json'
with open(filename, 'w') as f:
  json.dump(fav_num, f)

with open(filename) as f:
  fav_num = json.load(f)
  print(f"I know your favorite number! It's {fav_num}.")

  