# Three Restaurants

# Start with your class from Exercise 9-1. Create three different instances from the class, and call 'describe_restaurant()' for each instance.

class Restaurant:
  """Creating a class to represent a restaurant."""

  def __init__(self, name, cuisine):
    """Initializing the restaurant and cuisine."""
    self.name = name.title()
    self.cuisine = cuisine.title()
  
  def describe_restaurant(self):
    """Description of the Restaurant."""
    msg = f"{self.name} serves great {self.cuisine}!"
    print(f"\n{msg}")
  
  def open_restaurant(self):
    """Display a message that indicates restaurant is open."""
    msg = f"{self.name} is open. Come on in!"
    print(f"{msg}")

restaurant1 = Restaurant('tortilla factory', 'mexican')
restaurant2 = Restaurant('black sheep', 'american')
restaurant3 = Restaurant('filomena', 'italian')

print(restaurant1.name)
print(restaurant1.cuisine)
print(restaurant2.name)
print(restaurant2.cuisine)
print(restaurant3.name)
print(restaurant3.cuisine)

restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3.describe_restaurant()
restaurant3.open_restaurant()