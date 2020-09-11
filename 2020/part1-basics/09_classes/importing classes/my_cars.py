# From 'Importing Multiple Classes from a Module'

from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

# You import multiple classes from a module by separating each class with a comma (line 5). Once you've imported the necessary classes, you're free to make as many instances of each class as you need.

# In this example we make a regular Volkswagen Beetle at line 7 and an electric Tesla Roadster at line 10.