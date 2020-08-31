# Modifying an Attribute's Value Through a Method

# It can be helpful to have methods that update certain attributes for you. Instead of accessing the attribute directly, you pass the new value to a method that handles the updating internally.

# Here's an example showing a method called 'update_odometer()':

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

  # def update_odometer(self, mileage):
  #   """Set the odometer reading to the given value."""
  #   self.odometer_reading = mileage

# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())

# my_new_car.update_odometer(23)
# my_new_car.read_odometer()

# The only modification to 'Car' is the addition of 'update_odometer()' at line 25. This method takes in a milage value and assigns it to 'self.odometer_reading'. At line 32 we call 'update_odometer()' and give it 23 as an argument (corresponding to the 'mileage' parameter in the method definition). It sets the odometer reading to 23, and 'read_odometer() prints the reading.

# We can extend the method 'update_odometer()' to do additional work every time the odometer reading is modified. Let's add a little logic to make sure no one tries to roll back the odometer reading:

def update_odometer(self, mileage):
  """
  Set the odometer reading to the given value.
  Reject the change if it attempts to roll the odometer back.
  """
  if mileage >= self.odometer_reading:
    self.odometer_reading = mileage
  else:
    print("You can't roll back an odometer!")

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Now update_odometer() checks that the new reading makes sense before modifying the attribute. If the new mileage, 'mileage', is greater than or equal to the existing mileage, self.odometer_reading, you can update the odometer reading to the new mileage (line 44). If the new mileage is less than the existing mileage, you'll get a warning that you can't roll back an odometer (line 47).