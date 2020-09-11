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

# At line 9 we start with Car. When you create a child class, the parent class must be part of the current file and must appear before the child class in the file. At line 34 we define the child class, 'ElectricCar'. The name of the parent class must be included in parentheses in the definition of a child class. The __init()__ method at line 37 takes in the information required to make a 'Car' instance.

# The 'super()' function at line 39 is a special function that allows you to call a method from the parent class. This line tells Python to call the __init__() method from 'Car', which gives an 'ElectricCar' instance all the attributes defined in that method. The name 'super' comes from a convention of calling the parent class a 'superclass' and the child class a 'subclass'.

# We test whether inheritance is working properly by trying to create an electric car with the same kind of information we'd provide when making a regular car. At line 41 we make an instance of the 'ElectricCar' class and assign it to 'my_tesla'. This line calls the __init__() method defined in the parent class 'Car'. We provide the arguments 'tesla', 'model s', and 2019.

# Aside from __init__(), there are no attributes or methods yet that are particular to an electriv car. At this point we're just making sure the electric car has an appropriate Car behaviors.

# The 'ElectricCar' instance works just like an instance of 'Car', so now we can begin defining attributes and methods specific to electric cars.