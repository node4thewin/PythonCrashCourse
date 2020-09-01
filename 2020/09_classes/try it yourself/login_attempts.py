# 9-5 Login Attempts

# Add an attribute called 'login_attempts' to your 'User' class from Exercise 9-3 (page 162) Write a method called increment_login_attempts()' that increments the value of 'login_attempts' by 1. Write another method called 'reset_login_attempts()' that resets the value of 'login_attempts' to 0.

# Make an instance of the 'User' class and call 'increment_login_attempts()' several times. Print the value of 'login_attempts' to make sure it was incremented properly, and then call 'reset_login_attempts()'. Print 'login_attempts' again to make sure it was reset to 0.

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

user1 = User('andrew', 'harvey', 'ctrlshftejct', 32)
print(user1.login_attempts)

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.read_login_attempts()

user1.reset_login_attempts()
user1.read_login_attempts()