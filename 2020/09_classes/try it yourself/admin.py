# 9-7 Admin

# An administrator is a special kind of user. Write a class called 'Admin' that inherits from the from the 'User' class you wrote in Exercise 9-3 (page 162) or Exercise 9-5 (page 167). Add an attribute, 'privileges', that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. Write a method called 'show_privileges()' that lists the administrator's set of privileges. Create an instance of 'Admin', and call you method.

class User:
  """Define a User."""

  def __init__(self, first_name, last_name, username, age):
    """Initialize user profile and information."""
    self.first_name = first_name.title()
    self.last_name = last_name.title()
    self.username = username
    self.age = age
    self.login_attempts = 0

  def describe_user(self):
    """Print a summary of the user's information."""
    print("\n\tUser Information:\n")
    print(f"Name: {self.first_name} {self.last_name}")
    print(f"Username: {self.username}")
    print(f"Age: {self.age}")
  
  def greet_user(self):
    """Display a greeting to user."""
    msg = f"Greetings {self.username}!!! Welcome to the clan."
    print(msg)

  def increment_login_attempts(self):
    """Increment login attempts by 1."""
    self.login_attempts += 1
  
  def reset_login_attempts(self):
    """Reset login attempts to zero."""
    self.login_attempts = 0

  def read_login_attempts(self):
    """Display a message showing login attempts for user."""
    msg = f"{self.username} has attempted to login {self.login_attempts} times."
    print(msg)

class Admin(User):
  """Define User/Admin Privileges."""

  def __init__(self, first_name, last_name, username, age):
    """Initialize the admin."""
    super().__init__(first_name, last_name, username, age)

    self.privileges = Privileges()

class Privileges:
  """A class to store privileges."""

  def __init__(self, privileges=[]):
    "Initialize list of privileges."""
    self.privileges = privileges
  
  def show_privileges(self):
    """Display privileges."""
    print("\nPrivileges:")
    if self.privileges:
      for privilege in self.privileges:
        print(f"- {privilege}")
    else:
      print("- This user has no privileges.")

user1 = Admin('andrew', 'harvey', 'evrythngevl', 32)
user1.describe_user()

user1.privileges.show_privileges()

print("\nAdding privileges")
user1_privileges = [
  'can reset passwords',
  'can moderate discussions',
  'can suspend accounts',
]

user1.privileges.privileges = user1_privileges
user1.privileges.show_privileges()