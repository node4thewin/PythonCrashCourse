# We need to combine these two programs into one file. When someone runs 'remember_me.py' we want to retrieve their username from memory if possible; therefore, we'll start with a 'try' block that attempts to recover the username. If the file 'username.jason' doesn't exist, we'll have the 'except' block prompt for a username and store it in 'username.json' for next time.

import json

# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.

filename = 'username.json'
try:
  with open(filename) as f:
    username = json.load(f)

except FileNotFoundError:
  username = input("What is your name? ")
  with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!")

else:
  print(f"Welcome back, {username}!")

