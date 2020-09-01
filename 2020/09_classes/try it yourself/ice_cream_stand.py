# 9-6 Ice Cream Stand

# An ice cream stand is a specific kind of restaurant. Write a class called 'IceCreamStand' that inherits from the 'Restaurant' class you wrote in Exercise 9-1 (page 162) or Excercise 9-4 (page 167). Either version of the class will work; just pick the one you like better. Add an attribute called 'flavors' that stores a list of ice cream flavors. Write a method that displays these flavors. Create an instance of 'IceCreamStand', and call this method.

class IceCreamStand:
  """Display details about an Ice Cream Stand."""

  def __init__(self, name, location):
    """Initialize name and list of ice cream flavors"""
    self.name = name.title()
    self.location = location.title()
    self.flavors = [
      'chocolate', 'vanilla', 'coffee', 'strawberry', 'blueberry'
      ]

  def define_stand(self):
    """Describe the Ice Cream Stand."""
    print(f"\nName: \n  - {self.name}")
    print(f"Location: \n  - {self.location}")

  def display_flavors(self):
    """Display list of flavors"""
    print("Flavors:")
    for flavor in self.flavors:
      msg = f"  - {flavor.title()}"
      print(msg)

icecreamstand1 = IceCreamStand("carousels", 'warrenton')

icecreamstand1.define_stand()
icecreamstand1.display_flavors()