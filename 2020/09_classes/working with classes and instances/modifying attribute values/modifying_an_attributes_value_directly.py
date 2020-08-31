# Modifying an Attribute's Value Directly

# The simplest way to modify the value of an attribute is to access the attribute directly through an instance. Here we set the odometer reading to 23 directly:

class Car:
  
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
  
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# At line 26 we use dot notation to access the car's odometer_reading attribute and set its value directly This line tells Python to take the instance 'my_new_car', and find the attribute 'odometer_reading' associated with it, and set the value of that attribute to 23.

# Sometimes you'll want to access the attributes directly like this, but other times you'll want to write a method that updates the value for you.