# The 'Car' Class

# Let's write a new class representing a car. Our class will store information about the kind of car we're workign with, and it will have a method that summarizes this information:

class Car:
  """A simple attempt to represent a car."""
  
  def __init__(self, manufacturer, model, year):
    """Initialize attributes to describe a car."""
    self.manufacturer = manufacturer
    self.model = model
    self.year = year
  
  def get_descriptive_name(self):
    """Return a neatly formatted descriptive name."""
    long_name = f"{self.year} {self.manufacturer} {self.model}"
    return long_name.title()

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

# At line 8 in the 'Car' class, we define the __init__() method with the self parameter first, just like we did before with our 'Dog' class. We also give it three other parameters: make, model, and year. The __init__() method takes in these parameters and assigns them to the attributes that will be associated with instances made from this class. When we make a new 'Car' instance, we'll need to specify a make, model, and year for our instance.

# At line 14, we define a method called 'get_descriptive_name()' that puts a car's year, make, and model into one string neatly describing the car. This will spare us from having to print each attribute's value individually. To work with the attribute values in this method, we use self.make, self.model, and self.year. At line 19 we make an instance from the 'Car' class and assign it to the variable 'my_new_car'. Then we call 'get_descriptive_name()' to show what kind of car we have.

# To make the class more interesting, let's add an attribute that changes over time. We'll add an attribute that stores the car's overall mileage.