# 9-1 Restaurant

# Make a class called 'Restaurant'. The __init__() method for 'Restaurant' should store two attributes: a 'restaurant_name' and a 'cuisine_type'. Make a method called 'describe_restaurant()' that prints these two pieces of information and a method called 'open_restaurant()' that prints a message indicating that the restaurant is open.

# Make an instance called 'restaurant' from your class. Print the two attributes individually, and then call both methods.

class Restaurant:
  """Indicate a Restaurant is Open or Closed."""

  def __init__(self, name, cuisine):
    """Initialize name, cuisine, and if open or closed."""
    self.name = name.title()
    self.cuisine = cuisine.title()
  
  def describe_restaurant(self):
    """Display a summary of the restaurant."""
    msg = f"{self.name} serves great {self.cuisine}!"
    print(f"\n{msg}")

  def open_restaurant(self):
    """Display a message that the restaurant is open."""
    msg = f"{self.name} is open. Come on in!"
    print(f"\n{msg}")

restaurant = Restaurant('tortilla factory', 'mexican')
print(restaurant.name)
print(restaurant.cuisine)

restaurant.describe_restaurant()
restaurant.open_restaurant()