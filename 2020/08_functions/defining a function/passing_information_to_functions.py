# PASSING INFORMATION TO A FUNCTION

# Modified slightly, the function 'greet_user()' can not only tell the user 'Hello!' but also green them by name. For the function to do this, you enter 'username' in the parentheses of the function's definition at 'greet_user()'. By adding 'username' here you allow the function to accept any value of 'username' you specify. The function now expects you to provide a value for 'username' each time you call it. When you call 'greet_user()', you can pass it a name, such as 'jesse', inside the parentheses.

def greet_user(username):
  """Display a simple greeting."""
  print(f"Hello, {username.title()}!")

greet_user('jesse')

# Entering 'greet_user('jesse')' calls 'greet_user()' and gives the function the information it needs to execute the print() call. The function accepts the name you passed it and displays the greeting for that name.

# Likewise, entering 'greet_user('sarah') calls greet_user(), passes it 'sarah', and prints "Hello, Sarah!". You can all 'greet_user()' as often as you want and pass it any name you want to produce a predictable output every time.

greet_user('sarah')
greet_user('erika')
greet_user('callie')