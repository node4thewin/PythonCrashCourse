# Is Your Birthday Contained in Pi?

# I've always been curious to know if my birthday appears anywhere in the digits of 'pi'. Let's use the program we just wrote to find out if someone's birthday appears anywhere in the first million digits of 'pi'. We can do this by expressing each birthday as a string of digits and seeing if the string appears anywhere in 'pi_string':

filename = '/Users/andrewharvey/Github/PythonCrashCourse/ehmatthes-pcc_2e-078318e/chapter_10/pi_million_digits.txt'

with open(filename) as file_object:
  lines = file_object.readlines()

pi_string = ''
for line in lines:
  pi_string += line.strip()

birthday = input("Enter you birthday, in the form mmddyy: ")
if birthday in pi_string:
  print("You birthday appears in the first million digits of pi!")
else:
  print("Your birthday does not appear in the first million digits of pi.")

# At line 14 we prompt for the user's birthday, and then line 15 we check if that string is in 'pi_string'. Let's try it.

# My birthday does appear in the digits of 'pi'. Once you've read from a file, you can analyze its contents in just about any way you can imagine.