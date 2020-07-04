# DEFINING A TUPLE

# A tuple looks like a list except you use parentheses instead of square brackets. Once you define a tuple, you can access individual elements by using each item's index, just as you would for a list.

# For example, if we have a rectangle that should always be certain size, we can ensure that its size doesn't change by putting the dimentions into a tuple:

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# We define the tuple 'dimensions' in line 7, using parentheses instead of square brackets. At line 8 we print each element in the tuple individually, using the same syntax we've been using to access elements in a list:

# Let's see what happens if we try to change one of the items in the tuple 'dimensions':

dimensions[0] = 250

# This is beneficial because we want Python to raise an error when a line of code tries to change the dimensions of the rectangle.

# NOTE: Tuples are technically defined by the presence of a comma; the parentheses make them look neater and more readable. If you want to define a tuple with one element, you need to include a trailing comma:

my_t = (3,)

# It doesn't often make sense to build a tuple with one element, but this can happen when tuples are generated automatically.


