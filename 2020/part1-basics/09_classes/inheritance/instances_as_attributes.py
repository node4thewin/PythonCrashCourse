# Instances as Attributes

# When modeling something from the real world in code, you may find that you're adding more and more detail to a class. You'll find that you have a growing list of attributes and methods and that your files are becoming lengthy. In these situations, you might want to recognize that part of one class can be written as a separate class. You can break your large class into smaller classes that work together.

# For example, if we continue adding detail to the 'ElectricCar' class, we might notice that we're adding many attributes and methods specific to the car's battery. When we see this happening, we can stop and move those attributes and methods to a separate class called 'Battery'. Then we can use a 'Battery' instance as an attribute in the 'ElectricCar' class:

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

class Battery:
  """A simple attempt to model a battery for an electric car."""

  def __init__(self, battery_size=75):
    """Initialize the battery's attributes."""
    self.battery_size = battery_size
  
  def describe_battery(self):
    """Print a statement describing the battery size."""
    print(f"This car has a {self.battery_size}-kWh battery.")
  
  def get_range(self):
    """Print a statement about the range this battery provides."""
    if self.battery_size == 75:
      range = 260
    
    elif self.battery_size == 100:
      range = 315
    
    print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
  """Represent aspects of a car, specific to electric vehicles."""
  def __init__(self, make, model, year):
    """
    Initialize attributes of the parent class.
    Then initialize attributes specific to an electric car.
    """
    super().__init__(make, model, year)
    self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

# At line 32 we define a new class called 'Battery' that doesn't inherit from any other class. The __init__() method at line 35 has one parameter, 'battery_size', in addition to 'self'. This is an optional parameter that sets the batter's size to 75 if no value is provided. The method 'describe_battery()' has been moved to this class as well (line 39).

# In the 'ElectricCar' class, we now add an attribute called 'self.battery' (line 51). This line tells Python to create a new instance of 'Battery' (with a default size of 75, becuase we're not specifying a value) and assign that instance to the attribute 'self.battery'. This will happen every time the __init__() method is called; any 'ElectricCar' instance will now have a 'Battery' instance created automatically.

# We create an electric car and assign it to the variable 'my_tesla'. When we want to describe the battery, we need to work through the car's 'battery' attribute:

# my_tesla.battery.describe_battery()

# This line tells Python to look at the instance 'my_tesla', find its 'battery' attribute, and call the method 'describe_battery()' that's associated with the 'Battery' instance stored in the attribute.

# The output is identical to what we saw previously...

# This looks like a lot of extra work, but now we can describe the battery in as much detail as we want without cluttering the ElectricCar class. Let's add another method to 'Battery' that reports the range of the car based on the battery size.

my_tesla.battery.get_range()

# The new method 'get_range()' at line 43 performs some simple analysis. If the battery's capacity is 75 kWh, 'get_range()' sets the range to 260 miles, and if the capacity is 100kWh, it sets the range to 315 miles. It then reports this value. When we want to use this method, we again have to call it through the car's 'battery' attribute at line 81.

# The output tells us the range of the car based on its battery size...