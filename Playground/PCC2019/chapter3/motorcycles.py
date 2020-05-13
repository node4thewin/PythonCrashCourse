motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# How can you change the value of the first item? Or maybe
# the second?

# The code below changes the value of the first item,
# output should show that it is changed.

motorcycles[0] = 'ducati'
print(motorcycles)

# Adding Elements to the list is also known as...
#	APPENDing items on the list
#	When you append an item to a list it is added to the END

motorcycles.append('honda')
print(motorcycles)

# This adds 'honda' to the end of the list without affecting
# any of the other elements in the list.

# You can also use the append() method to easily build lists
# dynamically. Like starting with an empty list then add items
# to the list using a series of append() calls.

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

# Above is a common way to build lists, because often you don't
# know exactly what data your users will want to store in the
# program.

# INSERTING ELEMENTS INTO A LIST

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

# REMOVING ELEMENTS FROM THE LIST

# Using the del Statement

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

# Removing an Item using the pop() Method

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

# The pop() method can be useful when things are stored
# in chronological order. 

motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# Popping Items from any Position in a List, aka using it to
# remove an item from any position.

motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# If unsure whether to use the del statement or the pop() method,
# rememeber if you want to use it again, use pop(). If you don't...
# use del.

# Removing an Item by Value

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")




