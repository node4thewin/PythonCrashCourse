# Page 58 Chapter 4 

# You can create almost any set of numbers you want using the
# range() function. For example if you wanted to make a list of
# the first 10 square numbers. In Python, use (**) to represent
# exponents. See below

squares = []
for value in range(1, 11):
	square = value ** 2
	squares.append(square)

print(squares)

# You can also write this same code more concisely. See below

squares = []
for value in range(1, 11):
	squares.append(value**2)

print(squares)

# Decide which way to use, since one may be easier to read but the
# other may reduce clutter.
# KNOW THIS AND PLAY AROUND

# List Comprehensions

# The earlier approach for generating lists consisted of 3-4 lines
# of code. A 'list comprehension' allows you to generate the same
# list in just one line of code. A list comprehension combines the
# for loop and the creation of new elements into one line, and 
# automagically appends each new element. 

# LIST COMPREHENSIONS ARE NOT FOR BEGINNERS...practice this.

squares = [value**2 for value in range(1, 11)]
print(squares)