# 9-6 Ice Cream Stand

# An ice cream stand is a specific kind of restaurant. Write a class called 'IceCreamStand' that inherits from the 'Restaurant' class you wrote in Exercise 9-1 (page 162) or Excercise 9-4 (page 167). Either version of the class will work; just pick the one you like better. Add an attribute called 'flavors' that stores a list of ice cream flavors. Write a method that displays these flavors. Create an instance of 'IceCreamStand', and call this method.

class Restaurant:
  """Indicate a Restaurant is Open or Closed."""

  def __init__(self, name, cuisine, location):
    """Initialize name, cuisine, and if open or closed."""
    self.name = name.title()
    self.cuisine = cuisine.title()
    self.location = location.title()
  
  def describe_restaurant(self):
    """Display a summary of the restaurant."""
    msg = f"{self.name} serves great {self.cuisine}!"
    print(f"\n{msg}")

  def open_restaurant(self):
    """Display a message that the restaurant is open."""
    msg = f"{self.name} is open. Come on in!"
    print(f"\n{msg}")

class IceCreamStand(Restaurant):
  """Display details about an Ice Cream Stand."""

  def __init__(self, name, location, cuisine='ice cream'):
    """Initialize name and list of ice cream flavors"""
    super().__init__(name, cuisine, location)
    self.flavors = []

  def display_flavors(self):
    """Display list of flavors"""
    print(f"\nFlavors on the Menu:")
    for flavor in self.flavors:
      msg = f"  - {flavor.title()}"
      print(msg)

carousels = IceCreamStand("carousels", 'warrenton')
carousels.flavors = [
  'chocolate', 'vanilla', 'strawberry', 'coffee', 'blueberry'
]

carousels.describe_restaurant()
carousels.display_flavors()