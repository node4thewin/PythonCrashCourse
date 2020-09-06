# Using Exceptions to Prevent Crashes

# Handling errors correctly is especially important when the program has more work to do after the error occurs. This happens often in programs that prompt users for input. If the program responds to invalid input appropriately, it can prompt for more valid input instead of crashing.

# Let's create a simple calculator that does only division:

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
  first_number = input("\nFirst number: ")
  if first_number == 'q':
    break
  second_number = input("Second number: ")
  if second_number == 'q':
    break
  answer = int(first_number) / int(second_number)
  print(answer)

# This program prompts the user to input a 'first_number' (line 11) and, if the user does not enter 'q' to quit, a second number (line 14). We then divide these two numbers to get an answer (line 17). This program does nothing to handle errors, so asking it to divide by zero causes it to crash...

# It's bad that the program crashed, but it's also not a good idea to let users see tracebacks. Nontechnical users will be confused by them, and in a malicious setting, attackers will learn more than you want them to know from a traceback. For example, they'll know the name of your program file, and they'll see a part of your code that isn't working properly. A skilled attacker can sometimes use this information to determine which kind of attacks to use against your code.