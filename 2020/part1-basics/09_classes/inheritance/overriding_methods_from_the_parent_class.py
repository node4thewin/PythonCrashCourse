# Overriding Methods from the Parent Class

# You can override any method form the parent class that doesn't fit waht you're trying to model with the child class. To do this, you define a method in the child class with the same name as the method you want to override in the parent class. Python will disregard the parent class method and only pay attention to the method you define in the child class.

# Say the class 'Car' had a method called 'fill_gas_tank()'. This method is meaningless for an all-electric vehicle, so you might want to override this method. Here's one way to do that:

class ElectricCar(Car):
  # -- snip -- 

  def fill_gas_tank(self):
    """Electric cars don't have gas tanks."""
    print("This car doesn't need a gas tank!")

# Now if someone tries to call 'fill_gas_tank()' with an electric car, Python will ignore the method 'fill_gas_tank()' in 'Car' and run this code instead. When you use inheritance, you can make you child classes retain what you need and override anything you don't need from the parent class.