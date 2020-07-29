# 5-9 NO USERS

# Add an 'if' test to 'hello_admin.py' to make sure the list of users is not empty.

# If the list is empty, print the message "We need to find some damn users!"

# Remove all of the usernames from your list, and make sure the correct message is printed.

usernames = []

# nested the for loop inside the username 'if' statement so I could add another 'else' condition.
if usernames:
  for username in usernames:
    if username == 'admin':
      print(f"Whatup Whatup {username}. Would you like to see the status report?")
    
    else:
      print(f"Welcome back {username}. Thanks for logging back in.")
else:
  print("We need some damn users!")