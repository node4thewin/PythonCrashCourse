# Importing a Single Class

# Let's create a module containing just the 'Car' class. This brings up a subtle naming issue: we already have a file named car.py in this chapter, but this module should be named car.py because it contains code representing a car. We'll resolve this naming issue by storing the 'Car' class in a module named 'car.py' replacing the 'car.py' file we were previously using. From now on, any program that uses this module will need a more specific filename, such as my_car.py Here's 'car.py' with just the code from the class Car:

"""A class that can be used to represent a car."""

class Car: