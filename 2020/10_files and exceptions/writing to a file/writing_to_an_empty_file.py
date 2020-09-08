# Writing to an Empty File

# To write text to a file, you need to call 'open()' with a second argument telling Python that you want to write to the file. To see how this works, let's write a simple message and store it in a file instead of printing it to the screen:

filename = 'programming.txt'

with open(filename, 'w') as file_object:
  file_object.write("I love programming.")

# The call to 'open()' in this example has two arguments (line 7). The first argument is still the name of the file we want to open. The second argument, 'w', tells Python that we want to open the file in 'write mode'. You can open a file in 'read mode' ('r'), write mode ('w'), append mode ('a'), or a mode that allows you to read and write to the file ('r+'). If you omit the mode argument, Python opens the file in read-only mode by default.

# The open() function automatically creates the file you're writing to if it doesn't already exist. However be careful opening a file in 'write' mode ('w') because if the file does exist, Python will erase the contents of the file before returning the file object.

# At line 8 we use the 'write()' method on the file object to write a string to the file. This program has no terminal output, but if you open the file 'programming.txt', you'll see one line:

# This file behaves like any other file on your computer, You can open it, write new text in it, copy from it, paste to it, and so forth.

# NOTE - Python can only write strings to a text file. If you want to store numerical data in a text file, you'll have to convert the data to string format first using the 'str()' function.