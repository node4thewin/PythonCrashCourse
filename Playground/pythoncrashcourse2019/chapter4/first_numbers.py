# MAKING NUMERICAL LISTS

# There are many reasons to store numbers. For example,
# keeping track of a players high scores. In data visualizations,
# you'll almost always work with sets of numbers, such as
# temperatures, distances, population sizes, or latitude and
# longitude values, among other types of numerical sets.

# Lists are ideal for storing sets of numbers, and Python provides
# a variety of tools to help you work efficiently with lists of
# numbers. Understand this and your code will work even when lists
# contain millions of items.

# Using the range() function...

for value in range(1, 5):
	print(value)

# Why doesn't this print the number 5? The range() function causes
# Python to start counting at the first value you give it, and it
# stops when it reaches the second value you provide. Since it stops
# at the second value, the output never contains the end value,
# which would have been 5 in this case.

# To print the numbers 1 through 5, you would use range(1, 6):

for value in range(1, 6):
	print(value)

# REMEMBER if your output is differnet than what you're expecting
# when you're using range(), try adjusting your value by 1.

# You can also pass range() only one argument and it will start
# a sequence of numbers at 0. See below

for value in range(6):
	print(value)


