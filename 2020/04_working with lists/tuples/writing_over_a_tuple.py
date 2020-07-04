# WRITING OVER A TUPLE

# Although you can't modify a tuple, you can assign a new value to a variable that represents a tuple. So if we wanted to change our dimensions, we could redefine the entire tuple:

dimensions = (200,50)
print("Original dimensions:")
for dimension in dimensions:
  print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
  print(dimension)

# The lines starting at line 5 define the original tuple and print the initial dimensions. At line 10, we associate a new tuple with the variable 'dimensions'. We then print the new dimensions at line 13. Python doesn't raise any errors this time, because reassigning a variable is valid.

# When compared with lists, tuples are simple data structures. Use them when you want to store a set of values that should not be changed throughout the life of a program.
