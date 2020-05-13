# INTRO TO DICTIONARIES

# A "dictionary" in Python is a collection of key-value pairs.
# Each "key" is connected to a value, and you can use a key to
# access the value associated with that key. A key's value can
# be a number, a string, a list, or even another dictionary. In
# fact, you can use any object that you can create in Python as
# a value in a dictionary.

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

# The simplest dictionary has exactly one key-value pair, as shown
# in this modified version of the alien_0 dictionary:

alien_0 = {'color' : 'green'}

# This dictionary stores one piece of information about alien_0,
# namely the alien's color. The string 'color' is a key in this
# dictionary, and its associated value is 'green'.

# ACCESSING VALUES IN A DICTIONARY
# To get the value associated with a key, give the name of the dictionary
# and then place the key inside of the set of square brackets, as shown
# here:

alien_0 = {'color': 'green'}
print(alien_0['color'])

# You can have an unlimited number of key-value pairs in a dictionary.
# For example, here's the original alien_0 dictionary with two key-value
# pairs:

alien_0 = {'color': 'purple', 'points': 5}
new_points = alien_0['points']
print(f"\nYou just earned {new_points} points!")

alien_1 = {'color': 'pink', 'points': 25000}
newer_points = alien_1['points']
print(f"\nYou just earned {newer_points} points!")


