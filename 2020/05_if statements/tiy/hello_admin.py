# 5-8 HELLO ADMIN

# Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user:

# If the username is 'admin', print a special greeting, such as "Hello 'admin', would you like to see the status report?"

# Otherwise print a generic greeting, such as "Hello Jaden, thank you for logging in again."

usernames = [
  'admin', 'j0llyjiM', 'ctrlshftejt', 'bieberh0le69', 'butte_stuff22', 'jam_and_java62'
  ]

# Loop through the list and print a greeting to each user:
for username in usernames:
  # if username is 'admin' print a special greeting
  if username == 'admin':
    print(f"Whatup Whatup {username}. Would you like to see the status report?")
  # otherwise print generic greeting
  else:
    print(f"Welcome back {username}. Thanks for logging back in.")