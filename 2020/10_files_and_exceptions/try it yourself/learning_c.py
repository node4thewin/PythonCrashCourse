# 10-2 Learning C

# You can use the 'replace()' method to replace any word in a string with a different word. Here's a quick example showing how to replace 'dog' with 'cat' in a sentence:

message = "I really like dogs."
print(message)
message.replace('dog', 'cat')
print(message)

# Read each line from the file you just created, 'learning_python.txt', and replace the word 'Python' with the name of another language, such as C. Print each modified line to the screen.

filename = 'learning_python.txt'

print("\n ---Reading lines and replacing Python with C:")
with open(filename) as f:
  lines = f.read()
  print(lines.replace('Python', 'C'))