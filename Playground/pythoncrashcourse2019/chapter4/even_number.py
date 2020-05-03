# Using range() to Make a List of Numbers

# If you want to make a list you can convert the results of
# range() into a list using the list() function. When you wrap
# list() around a range() function, the output will be a list of
# numbers. See below.

numbers = list(range(1, 6))
print(numbers)

# We can also use the range() function to tell Python to skip
# numbers in a given range. If you pass a third argument to range(),
# Python uses that value as a step size when generating numbers.

# Here is how to list even numbers between 1 and 10 (remember that
# you must have the extra number to accomodate for 10.)

even_numbers = list(range(2, 11, 2))
print(even_numbers)
