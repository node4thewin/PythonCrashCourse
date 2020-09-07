# Now let's write a new program that greets a user whose name has already been stored:

import json

filename = 'username.json'

with open(filename) as f:
  username = json.load(f)
  print(f"Welcome back, {username}!")

# At line 8 we use 'json.load()' to read the information stored in 'username.json' and assign it to the variable 'username'. Now that we've recovered the username, we can welcome them back (line 9).

# We need to combine these two programs into one file. When someone runs 'remember_me.py' we want to retrieve their username from memory if possible; therefore, we'll start with a 'try' block that attempts to recover the username. If the file 'username.jason' doesn't exist, we'll have the 'except' block prompt for a username and store it in 'username.json' for next time.

# Go to remember_me.py ...