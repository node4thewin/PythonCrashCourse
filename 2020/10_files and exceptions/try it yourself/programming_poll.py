# 10-5 Programming Poll

# Write a 'while' loop that asks people why they like programming. Each time someone enters a reason, add their reason to a file that stores all the responses.

fn = 'programming_poll.txt'

while True:
  print("Type 'quit' at any time to end the program.")
  poll = input("\nWhy do you like programming? ")

  if poll == 'quit':
    break
  else:
    with open('programming_poll.txt', 'a') as f:
      f.write(f"{poll}\n")