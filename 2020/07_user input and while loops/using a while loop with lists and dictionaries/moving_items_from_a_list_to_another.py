# MOVING ITEMS FROM ONE LIST TO ANOTHER

# Consider a list of newly registered but unverified users of a website. After we verify these users, how can we move them to a separate list of confirmed users? One way would be to use a 'while' loop to pull users from the list of unconfirmed users as we verify them and then add them to a separate list of confirmed users. Here's what that code might look like.

# Start with users that need to be verified,
# and an empty list to hold confirmed users.

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
  current_user = unconfirmed_users.pop()

  print(f"Verifying user: {current_user.title()}")
  confirmed_users.append(current_user) # add current_user to confirmed_users

# Display all confirmed users.
print("\nThe following users have been confirmed:")
# Use a 'for' loop to accomplish this.
for confirmed_user in confirmed_users:
  print(confirmed_user.title())

# We begin with a list of unconfirmed users at Line 8 (Alice, Brian, and Candace) and an empty list 