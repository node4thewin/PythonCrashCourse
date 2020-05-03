# Tuples

# Lists work well for storing collections of items/things that can
# change throughout the life of a program. The ability to modify
# lists is particularly important when you're working with a list of
# users on a website or a list of characters in a game. However,
# sometimes you'll want to creat a list of items that cannot
# change. Tuples allow you to do just that. Python refers to values
# that cannot change as immutable, and an immutable list is called
# a tuple.

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Let's see what happens if we try to change one of the items in
# in the tuple "dimensions":

# Looping Through All Values in a Tuple

# You can loop over all the values in a tuple using a for loop, just
# as you did with a list:

dimensions = (200, 50)
for dimension in dimensions:
	print(dimension)

# Writing over a Tuple

# Although you can't modify a tuple, you can assign a new value to
# a variable that represents a tuple. So if you wanted to change
# our dimensions, we could redefine the entire tuple:

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)

# Redefined Tuple

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)



