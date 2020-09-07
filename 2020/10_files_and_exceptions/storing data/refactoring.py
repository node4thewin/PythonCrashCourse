# Refactoring

# Often, you'll come to a point where your code will work, but you'll recognize that you could improve the code by breaking it up into a series of functions that have specific jobs. This process is called 'refactoring'. Refactoring makes your code cleaner, easier to understand, and easier to extend.

# We can refactor remember_me.py by moving the bulk of its logic into one or more functions. The focus of 'remember_me.py' is on greeting the user, so let's move all of our existing code into a function called 'greet_user()':

# import json

# def greet_user():
#   """Greet the user by name."""
#   filename = 'username.json'
#   try:
#     with open(filename) as f:
#       username = json.load(f)
#   except FileNotFoundError:
#     username = input("What is your name: ")
#     with open(filename, 'w') as f:
#       json.dump(username, f)
#       print(f"We'll remember when you come back, {username}!")
#   else:
#     print(f"Welcome back, {username}!")

# greet_user()

# Because we're using a function now, we update the comments with a docstring that reflects how the program currently works (line 10). This file is a little cleaner, but the function greet_user() is doing more than just greeting the user--it's also retrieving a stored username if one exists and prompting for a new username if one doesn't exist. 

# Let's refactor 'greet_user()' so it's not doing so many different tasks. We'll start by moving the code for retrieving a stored username to a separate function:

import json

def get_stored_username():
  """Get stored username if available."""
  filename = 'username.json'
  try:
    with open(filename) as f:
      username = json.load(f)
  except FileNotFoundError:
    return None
  else:
    return username

import json

def greet_user():
  """Greet the user by name."""
  username = get_stored_username()
  if username:
    print(f"Welcome back, {username}!")
  else:
    username = input("What is your name: ")
    filename = 'username.json'
    with open(filename, 'w') as f:
      json.dump(username, f)
      print(f"We'll remember you when you come back, {username}!")

greet_user()

# The new function 'get_stored_username()' has clear purpose, as stated in the docstring (line 32). This function retrieves a stored username and returns the username if it finds one. If the file 'username.json' doesn't exist, the function returns 'None' (line 38). This is good practice: a function should either return the value you're expecting, or it should return 'None'. This allows us to perform a single test with the return value of the function. At line 47 we print a welcome back message to the user if the attempt to retrieve a username was successful, and if it doesn't, we prompt for a new username.

# We should factore one more black of code out of 'greet_user()' If the username doesn't exist, we should move the code that prompts for a new username to a function dedicated to that purpose:

