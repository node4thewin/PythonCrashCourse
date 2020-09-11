# Large Files: One Million Digits

# So far we'ved focused on analyzing a text file that contains only three lines, but the code in these examples would work just as well on much larger files. If we start with a text file that contains 'pi' to 1,000,000 decimal places instead of just 30, we can create a single string containing all these digits. We don't need to change our program at all except to pass it a different file. We'll also print just the first 50 decimal places, so we don't have to watch a million digits scroll by in the terminal:

filename = '/Users/andrewharvey/Github/PythonCrashCourse/ehmatthes-pcc_2e-078318e/chapter_10/pi_million_digits.txt'

# this shows how to go get a file from another directory

with open(filename) as file_object:
  lines = file_object.readlines()

pi_string = ''
for line in lines:
  pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

# Python has no inherent limit to how much data you can work with; you can work with as much data as your system's memory can handle.

# NOTE - to run this program (an many of the examples that follow), you'll need to download the resources available at https://nostarch.com/pythoncrashcourse2e/