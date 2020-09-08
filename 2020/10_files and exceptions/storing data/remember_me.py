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

# There's no new code here; blocks of code from the last two examples are just combined into one file. At line 10 we try to open the file 'username.json'. If this file exists, read the username back into memory (line 11) and print a message welcoming back the user in the 'else' block. If this is the first time the user runs the program, 'username.json' won't exist and a 'FileNotFoundError' will occur (line 13). Python will move on to the 'except' block where we prompt the user to enter their username (line 14). We then use 'json.dump()' to store the username and print a greeting (line 15).

# This is the output you see if the program was already run at least once.