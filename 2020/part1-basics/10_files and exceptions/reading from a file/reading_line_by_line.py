# Reading Line by Line

# When you're reading a file, you'll often want to examine each line of the file. You might want to modify the text in the file in some way. For example, you might want to read through a file of weather data and work with any line that includes the word 'sunny' in the description of that day's weather. In a news report, you might look for any line with the tag <headline> and rewrite that line with a specific kind of formatting.

# You can use a 'for' loop on the file object to examine each line from a file one at a time:

filename = 'pi_digits.txt'

# with open(filename) as file_object:
#   for line in file_object:
#     print(line)

# At line 7 we assign the name of the file we're reading from to the variable 'filename'. This is a common convention when working with files. Because the variable 'filename' doesnt represent the actual file--it's just a string telling Python where to find the file--you can easily swap out 'pi_digits.txt' for the name of another file you want to work with. After we call open(), an object representing the file and its contents is assigned to the variable 'file_object' (line 9). We again use the 'with' syntax to let Python open and close the file properly. To examine the file's contents, we work through each line in the file by looping over the file object (line 10). 

# When we print each line, we find even more blank lines. These blank lines appear beacuse an invisible newline character is at the end of each line in the text file. The 'print' function adds its own new-line each time we call it, so we end up with two newline characters at the end of each line:

with open(filename) as file_object:
  for line in file_object:
    print(line.rstrip())