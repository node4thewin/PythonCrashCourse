# ADDING ELEMENTS TO A LIST

# You might want to add a new element to a list for many reason. For example, you might want
# to make new aliens appear in a game, add new data to a visualization, or add new registered
# users to a website you've built. Python provides several ways to add new data to existing
# lists.

# ADDING ITEMS TO THE END OF THE LIST (APPENDING)

# The simplest way to add a new element to a list is to "append" the item to the list. When
# you append an item to a list, the new element is added to the end of the list. Using the
# same list we had in the previous example, we'll add the new element 'ducati' to the end
# of the list:

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

# The append() method adds 'ducati' to the end of the list without affecting any of the other
# elements in the list.

# The append() method makes it easy to build lists dynamically. For example, you can start with
# an empty list and then add items to the list using a series of append() calls. Using an empty
# list, let's add the elements 'honda', 'jeep', 'toyota', and 'ford' to my list of cars I want:

cars = []
print(cars)

cars.append('honda')
cars.append('jeep')
cars.append('toyota')
cars.append('ford')
print(cars)

# Building list this way is very common, because you often won't know the data your users want
# to store in a program until after the program is running. To put your users in control, start
# by defining an empty list that will hold the users' values. Then append each new value provided
# to the list you just created.


