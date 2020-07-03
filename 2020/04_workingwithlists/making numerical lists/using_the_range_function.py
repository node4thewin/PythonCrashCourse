# USING THE RANGE() FUNCTION

# Python's range() function makes it easy to generate a series of numbers. For example, you can use the range() function to print a series of numbers like this:

for value in range(1, 5):
  print(value)

# Although this looks like it should print the numbers from 1-5, it doesn't print the number 5. This is another example of the off-by-one behavior you'll often see in programming languages. The range() function causes Python to start counting at the first value you give it, and it stops when it reaches the second value you provide. because it stops at the second value, the output never contains the end value, which would have been 5 in this case.

# To print the numbers from 1-5, you would use...

for value in range(1, 6):
  print(value)

# If your output is difference than what you expect when you're using range(), try adjusting your end value by 1. You can also pass range() only one argument, and it will start the sequence of numbers at 0. For example, range(6) would return the numbers 0-5.

for value in range(6):
  print(value)