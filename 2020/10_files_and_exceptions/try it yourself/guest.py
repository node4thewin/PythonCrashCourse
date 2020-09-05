# 10-3 Guest

# Write a program that prompts the user for their name. When they respond, write their name to a file called 'guest.txt'.

filename = 'guest.txt'

while True:
  print("Type 'quit' at anytime to end program.\n")
  guest = input("What's your name? ")
  if guest == 'quit':
    break
  else:
    with open(filename, 'w') as f:
      f.write(guest)