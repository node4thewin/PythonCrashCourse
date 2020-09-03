# Importing a Module into a Module (electric_car.py, car2.py, my_cars3.py)

# Sometimes you'll want to spread out your classes over several modules to keep any one file from gowing too large and avoid storing unrelated classes in the same module. When you store your classes in several modules, you may find that a class in one module depends on a class in another module. When this happens, you can import the required class into the first module.

# For example, let's store the Car class in one module and the ElectricCar and Battery classes in a separate module. We'll make a new module called 'electric_car.py'--replacing the 'electric_car.py' file we created earlier--and copy just the Battery and ElectricCar classes into this file:

"""A set of classes that can be used to represent electric cars."""

# from car import Car

# class Battery:
#   --snip--

# class ElectricCar(Car):
#   -- snip--

# The class ElectricCar needs access to its parent class Car, so we import Car directly into the module at line 9. If we forget this line, Python will raise an error when we try to import the 'electric_car' module. We also need to update the Car module so it contains only the Car class:

# Now we can import from each module separately and create whatever kind of car we need:

from car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2020)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2020)
print(my_tesla.get_descriptive_name())