# 10-7 Addition Calculator

# Wrap your code from Exercise 10-6 in a 'while' loop so the user can continue entering numbers even if they make a mistake and enter text instead of a number.

print("Enter 'quit' at anytime to end the program.")
print("Type any two numbers and we'll add them together...")

while True:
  first_number = input("\nFirst number: ")
  if first_number == 'quit':
    break
  
  second_number = input("Second number: ")
  if second_number == 'quit':
    break
  
  try:
    total = int(first_number) + int(second_number)
  except ValueError:
    print("Try again with numbers, not letters/strings.")

  else:
    print(f"The sum is {total}.")