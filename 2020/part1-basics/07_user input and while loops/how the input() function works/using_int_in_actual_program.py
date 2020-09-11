# USING INT() IN AN ACTUAL PROGRAM

# How do you use the 'int()' function in an actual program? Consider a program that determines whether people are tall enough to ride a rollercoaster:

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
  print("\nYou're tall enough to ride!")
else:
  print("\nYou'll be able to ride when you're a little older.")

# The program can compare height to 48 because 'height = int(height) converted the string input value to a numerical representation (integer) before the comparison is made. If the number entered is greater than or equal to 48, we tell the user that they're tall enough.

# When you use numerical input to do calculations and comparisons, be sure to convert the input value to a numerical representation first.