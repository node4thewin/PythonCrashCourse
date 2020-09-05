# Writing Multiple Lines

# The 'write()' function doesn't add any newlines to the text you write. So if you write more than one line without including newline characters, your file may not look the way you want it to:

filename = 'programming.txt'

# with open(filename, 'w') as file_object:
#   file_object.write("I love programming.")
#   file_object.write("I love creating new games.")

# If you open 'programming.txt' you'll see the two lines squished together. Including newlines in your calls to 'write()' makes each string appear on its own line:

with open(filename, 'w') as file_object:
  file_object.write("I love programming.\n")
  file_object.write("I love creating new games.\n")

# You can also use spaces, tab characters, and blank lines to format your output, just as you've been doing with terminal-based output.