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

    # Initialize an empty set of privileges.
    self.privileges = Privileges()

class Privileges:
  """A class to store an admin's privileges."""

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