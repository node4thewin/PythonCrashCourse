# for 'Importing an Entire Module'

import car

my_beetle = car.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

# At line 3 we import the entire car module. We then access the classes we need through the...

# module_name.ClassName syntax 

# At line 5 we again create a Volkswagen Beetle, and at line 8 we create a Tesla Roadster.