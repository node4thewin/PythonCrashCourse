# STARTING WITH AN EMPTY DICTIONARY

# It's sometimes convenient, or even necessary, to start with an empty dictionary and then add each new item to it. To start filling an empty dictionary, define a dictionary with an empty set of braces and then add each key-value pair on its own line. For example, here's how to build the 'alien_0' dictionary using this approach:

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# Here we define an empty 'alien_0' dictionary, and then add color and point values to it. The result is the dictionary we've been using in previous examples.

# Typically, you'll use empty dictionaries when storing user-supplied data in a dictionary or when you write code that generates a large number of key-value pairs automatically.