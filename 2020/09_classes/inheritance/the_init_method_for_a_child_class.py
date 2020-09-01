# THE __init__() METHOD FOR A 'Child' CLASS

# When you're writing a new class based on an existing class, you'll often want to call the __init__() method from the parent class. This will initialize any attributes that were defined in the parent __init__() method and make them available in the child class.

# As an example, let's model an electric car. An electric car is just a specific kind of car, so we can base our new 'ElectricCar' class on the 'Car' class we wrote earlier. Then we'll only have to write code for the attributes and behavior specific to electric cars.

# Let's start by making a simple version of the 'ElectricCar' class, which does everything 'Car' class does:

class Car:
  """A simple attempt to represent a car."""

  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0
  
  def get_descriptive_name(self):
    long_name = f"{self.year} {self.make} {self.model}"
    return long_name.title()
  
  def read_odometer(self):
    print(f"This car has {self.odometer_reading} miles on it.")
  
  def update_odometer(self, mileage):
    if mileage >= self.odometer_reading:
      self.odometer_reading = mileage
    else:
      print("You can't rolle back an odometer!")
  
  def increment_odometer(self, miles):
    self.odometer_reading += miles

class ElectricCar(Car):
  """Represent aspects of a car, specific to electric vehicles."""

  def __init__(self, make, model, year):
    """Initialize attributes of the parent Class."""
    super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())