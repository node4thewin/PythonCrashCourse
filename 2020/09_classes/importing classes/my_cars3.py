# from 'Importing a Module into a Module'

from car2 import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2020)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'beetle', 2020)
print(my_tesla.get_descriptive_name())