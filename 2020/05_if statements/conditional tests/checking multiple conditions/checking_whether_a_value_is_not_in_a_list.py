# CHECKING WHETHER A VALUE IS NOT IN A LIST

# Other times, it's important to know if a value does not appear in a list. You can use the keyword 'not' in this situation. For example, consider a list of users who are banned from commenting in a forum. You can check whether a user has been banned before allowing that person to submit a comment:

banned_users = [
  'bieberh0le69', 'mgharvest', 'evrythngevl'
  ]
user = 'bootyhole22'

if user not in banned_users:
  print(
    f"\nHello {user}. You can post a response if you wish. Don't be a dick!"
    )

