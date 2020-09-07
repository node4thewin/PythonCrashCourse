# Now we'll write a program that uses 'json.load()' to read the list back into memory:

import json

filename = 'numbers.json'
with open(filename) as f:
  numbers = json.load(f)

print(numbers)

# At line 5 we make sure to read from the same file we wrote to. This time when we open the file, we open it in read mode because Python only needs to read from the file (line 6). At line 7 we use the 'json.load()' function to load the information stored in 'numbers.json', and we assign it to the variable 'numbers'. Finally we print the recovered list of numbers and see that it's the same list created in 'number_writer.py'

# This is a simple way to share data between two programs.