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