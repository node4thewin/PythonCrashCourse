# USING RANGE() TO MAKE A LIST OF NUMBERS

# If you want to make a list of numbers, you can convert the results of range() directly into a list using the list() function. When you wrap list() around a call to the range() function, the output will be a list of numbers.

# In the example in the previous section, we simply printed out a series of numbers. We can use list() to convert that same set of numbers into a list:

numbers = list(range(1, 6))
print(numbers)

# We can also use the range() function to tell Python to skip numbers in a given range. If you pass a third argument to range(), Python uses that value as a step size when generating numbers. For example here's how to list the even numbers between 1 and 10:

even_numbers = list(range(2, 11, 2))
print(even_numbers)

# In this example the range() function starts with the value 2 and then adds 2 to that value. It adds 2 repeatedly until it reaches or passes the end value, 11, and produces this result [2, 4, 6, 8, 10]

# You can create almost any set of numbers you want using the range() function. For example, consider how you might make a list of the first 10 square numbers (that is, the square of each integer from 1 through 10). In Python, two asterisks(**) represent exponents. Here's how you might put the first 10 square numbers into a list:

squares = []
for value in range(1, 11):
  square = value ** 2
  squares.append(square)

print(squares)

# We start with an empty list called squares (line 19). At line 20, we tell Python to loop through each value from 1-10 using the range() function. Inside the loop, the current value is raised to the second power and assigned to the variable "square" (line 21). At Line 22, each new value of square is appended to the list "squares". Then when the loop is finally finished we print the list of "squares".

# However, to write this code more concisely, omit the temporary variable square and append each new value directly to the list:

new_squares = []
for new_value in range(1, 11):
  new_squares.append(new_value**2)
print(new_squares)

# The code at Line 32 does the same work as lines 21 and 22 in "squares". Each value in the loop is raised to the second power and then immediately appended to the list of squares.

# You can use either of these two approaches when you're making more complex lists. Sometimes using a temporary variable makes your code easier to read; other times it makes the code unnecessarily long. Focus first on writing code that you understand clearly, which does what you want it to do. Then look for more efficient approaches as you review your code.