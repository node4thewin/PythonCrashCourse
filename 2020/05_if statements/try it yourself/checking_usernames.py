# Checking Usernames

# Do the following to create a program that simulates how websites ensure that everyone has a unique username.

# Make a list of five or more usernames called 'current_users'
# Make another list of five usernames called 'new_users'. Make sure one or two of the new usernames are also in the current_users list.
# Loop through the 'new_users' list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying that the username is available.
# make sure your comparison is CASE INSENSITIVE. If 'John' has been used, 'JOHN' should not be accepted. (To do this you'll need to make a copy of current_users containing the lowercase versions of all existing users.)

current_users = [
  'admin', 'j0llyjiM', 'ctrlshftejt', 'bieberh0le69', 'butte_stuff22', 'jam_and_java62'
  ]

# make sure to change case on copied current_users so you can test
new_users = [
  'b0rderHo4rder', 'g3nderb3nder', 'orGasMask', 'ADMIN', 'JAM_AND_JAVA62'
]

if new_users:
  for new_user in new_users:
    if new_user.lower() in current_users:
      print(f"Hello...unfortunately {new_user} is taken. Please try another username.\n")
    else:
      print(f"Welcome to the club {new_user}! LFG!\n")
else:
  print("We need some damn users!")