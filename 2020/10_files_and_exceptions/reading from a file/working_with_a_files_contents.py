# Working with a File's Contents

# After you've read a file into memory, you can do whatever you want with that data, so let's briefly explore the digits of 'pi'. First we'll attempt to build a single string containing all the digits in the file with no whitespace in it:

filename = 'pi_digits.txt'

with open(filename) as file_object:
  lines = file_object.readlines()

pi_string = ''
for line in lines:
  pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

# We start by opening the file and storing each line of digits in a list, just as we did in the previous example. At line 10 we create a variable, 'pi_string', to hold the digits of 'pi'. We then create a loop that adds each line of digits to 'pi_string' and removes the newline character from each line (line 11). At line 14 we print this string and also show how long the string is...

# The variable 'pi_string' contains the whitespace that was on the left side of the digits in each line, but we can get rid of that by using 'strip()' instead of 'rstrip()':

filename = 'pi_digits.txt'

with open(filename) as file_object:
  lines = file_object.readlines()

pi_string = ''
for line in lines:
  pi_string += line.strip() # used strip so that every bit of whitespace was removed vs. just whitespace to the right (rstrip.())

print(pi_string)
print(len(pi_string))

# Now we have a string containing 'pi' to 30 decimal places. The string is 32 characters long because it also includes the leading 3 and a decimal point.

# NOTE - When Python reads from a text file, it interprets all text in the file as a string. If you read in a number and want to work with that value in a numerical context, you'll have to convert it to an integer using the 'int()' function or convert it to a float using the 'float()' function.

pi_string = float(pi_string)
print(pi_string + 1) # just to show that pi_string is now a float