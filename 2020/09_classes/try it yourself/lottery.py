# 9-14 Lottery

# Make a list or tuple containing a series of 10 numbers and five letters. Randomly select four numbers or letters from the list and print a message saying that any ticket matching these four numbers or letters win a prize.

from random import choice

possibilities = [1,2,3,4,5,6,7,8,9,10,'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

lottery_numbers = []
print("Let's see what the winning ticket is...")

# We don't want to repeat winning numbers so we'll use a while loop
while len(lottery_numbers) < 5:
  pulled_item = choice(possibilities)

  # Only add the pulled item to the winning ticket if it hasnt been pulled already
  if pulled_item not in lottery_numbers:
    print(f"  We pulled a {pulled_item}!")
    lottery_numbers.append(pulled_item)

print(f"The final winning ticket is: {lottery_numbers}")