# Importing a Single Class

# Let's create a module containing just the 'Car' class. This brings up a subtle naming issue: we already have a file named car.py in this chapter, but this module should be named car.py because it contains code representing a car. We'll resolve this naming issue by storing the 'Car' class in a module named 'car.py' replacing the 'car.py' file we were previously using. From now on, any program that uses this module will need a more specific filename, such as my_car.py Here's 'car.py' with just the code from the class Car:

"""A class that can be used to represent a car."""

class Car:
  """A simple attempt to represent a car."""

  def __init__(self, make, model, year):
    """Initialize attributes to describe a car."""
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0
  
  def get_descriptive_name(self):
    """Return a neatly formatted descriptive name."""
    long_name = f"{self.year} {self.make} {self.model}"
    return long_name.title()

  def read_odometer(self):
    """Print a statement showing the car's mileage."""
    print(f"This car has {self.odometer_reading} miles on it.")
  
  def update_odometer(self, mileage):
    """
    Set the odometer reading to the given value.
    Reject the change if it attempts to roll the odometer back.
    """
    if mileage >= self.odometer_reading:
      self.odometer_reading = mileage
    else:
      print("You can't roll back an odometer")
  
  def increment_odometer(self, miles):
    """Add the given amount to the odometer reading."""
    self.odometer_reading += miles

# At line 5 we include a module-level docstring that briefly describes the contents of this module. You should write a docstring for each module you create.

# Now we can make a separate file called 'my_car.py' This file will import the Car class and then create an instance from that class.

from car import Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# The import statement at line 1 tells Python to open the 'car' module and import the class 'Car'. Now we can use the 'Car' class as if it were defined in this file. The output is the same as we saw earlier.

# Importing classes is an effective way to program. Picture how long this program file would be if the entire 'Car' class were include. When you instead move the class to a module and import the module, you still get all the same functionality, but you can keep you main program file clean and easy to read. You also store most of the logic in separate files; once your classes work as you want them to, you can leave those files alone and focus on the higher-level logic of your main program.