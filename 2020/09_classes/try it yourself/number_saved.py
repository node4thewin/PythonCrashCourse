# Number Saved

# Start with your program from 9-1 (page 162). Add an attribute called 'number_served' with a default value of 0. Create an instance called 'restaurant' from this class. Print the number of customers the restaurant has served, and then change this value and print it again.

# Add a method called 'set_number_served()' that lets you set the number of customers that have been served. Call this method with a new number and print the value again.

# Add a method called increment_number_served()' that lets you increment the number of customers who've been served. Call this method with any number you like that could represent how many customers were served in, say, a day of business.

class Restaurant:
  """
  Indicate a Restaurant is Open or Closed.
  Show the number of customer the restaurant has served.
  """

  def __init__(self, name, cuisine):
    """Initialize name, cuisine, and if open or closed."""
    self.name = name.title()
    self.cuisine = cuisine.title()
    self.number_served = 0
  
  def describe_restaurant(self):
    """
    Display a summary of the restaurant.
    Include message about number of customers served.
    """
    msg = f"{self.name} serves great {self.cuisine}!"
    print(f"\n{msg}")
    msg2 = f"{restaurant.name} has now served {restaurant.number_served} customers."
    print(msg2)

  def open_restaurant(self):
    """Display a message that the restaurant is open."""
    msg = f"{self.name} is open. Come on in!"
    print(f"\n{msg}")
  
  def set_number_served(self, number_served):
    """
    Set the number of customers that have been served.
    Reject the number if it attempts to roll back the number of customers served.
    """
    if number_served >= self.number_served:
      self.number_served = number_served

    else:
      print("\nYou can't roll back the number of customers you've served!")

  def increment_number_served(self, new_served):
    """Add the given amount to the number served."""
    self.number_served += new_served

restaurant = Restaurant('Tortilla Factory', 'mexican')
restaurant.describe_restaurant()
print(f"{restaurant.name} has now served {restaurant.number_served} customers.")

restaurant.number_served = 456
print("\nUpdate:")
print(f"{restaurant.name} has now served {restaurant.number_served} customers.")

restaurant.set_number_served(466)
restaurant.set_number_served(465)

restaurant.increment_number_served(53)
restaurant.describe_restaurant()
