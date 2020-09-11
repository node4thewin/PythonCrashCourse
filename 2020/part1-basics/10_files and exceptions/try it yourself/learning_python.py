# 10-1 Learning Python

# Open a blank file in your text editor and write a few lines summarizing what you've learned about Python so far. Start each line with the phrase 'In Python you can...' Save the file as 'learning_python.txt' in the same directory as your exercises from this chapter. Write a program that reads the file and prints what you wrote three times. Print the contents once by reading in the entire file, once by looping over the file object, and once by storing the lines in a list and then working with them outside the 'with' block.

filename = 'learning_python.txt'

# Print the contents once by reading in the entire file
print("\n ---Reading the entire file:")
with open('learning_python.txt') as file_object:
  contents = file_object.read()
print(contents)

# Print by looping over the file object
print("\n ---Looping over theh file object:")
with open('learning_python.txt') as file_object:

  for line in file_object:
    print(line.rstrip())
  
# Store the line in a list and then work with them outside the 'with' block

print("\n ---Storing line in a list and using 'with' block:")
with open(filename) as f:
  lines = f.readlines()

for line in lines:
  print(line.rstrip())