# 10-4 Guest Book

# Write a 'while' loop that prompts users for their name. When they enter their name, print a greeting to the screen and add a line recording their visit in a file called 'guest_book.txt'. Make sure each entry appears on a new line in the file.

name = 'guest_book.txt'

while True:
  print("Type 'quit' at any time to end the program.")
  guest = input("Welcome! Record your name here: ")
  
  if guest == 'quit':
    break
  else:
    with open(name, 'a') as f:
      f.write(guest)
      f.write("\n")
