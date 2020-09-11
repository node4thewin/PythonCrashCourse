# Saving and Reading User-Generated Data

# Saving data with 'json' is useful when you're working with user-generated data, because if you don't store your user's information somehow, you'll lose it when the program stops running. Let's look at an example where we prompt the user for their name the first time they run a program and then remember their name when they run the program again.

# Let's start by storing the user's name:

import json

username = input("What is your username? ")

filename = 'username.json'
with open(filename, 'w') as f:
  json.dump(username, f)
  print(f"We'll remember you when you come back, {username}!")

# At line 9 we prompt the user for their username to store. Next we use 'json.dump()' passing it a username and a file object, to store the username in a file (line 13). Then we print a message informting the user that we've stored their information (line 14).

# Go to reading_user-generated_data.py...
