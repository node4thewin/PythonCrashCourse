# 9-3 Users

# Make a class called 'User'. Create two attributes called 'first_name' and 'last_name', and then create several other attributes that are typically stored in a user profile. Make a method called 'describe_user()' that prints a summary of the user's information. Make another method called 'greet_user()' that prints a personalized greeting to the user.

# Create several instances representing different users. and call both methods for each user.

class User:
  """Define a User."""

  def __init__(self, first_name, last_name, username, age):
    """Initialize user profile and information."""
    self.first_name = first_name.title()
    self.last_name = last_name.title()
    self.username = username
    self.age = age

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

user1 = User('andrew', 'harvey', 'ctrlshftejct', 32)
user2 = User('callie', 'barron', 'bieberh0le69', 27)
user3 = User('michael', 'harvey', 'mgharvest', 27)
user4 = User('michael', 'barron', 'slaKr86', 33)

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

user4.describe_user()
user4.greet_user()





