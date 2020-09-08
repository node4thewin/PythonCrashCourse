# The 'else' Block

# We can make this program more error resistant by wrapping the line that might produce errors in a 'try-except' block. The error occurs on the line that performs the division, so that's where we'll put the 'try-except' block. This example also includes an 'else' block. Any code that depends on the 'try' block executing successfully goes in the 'else' block:

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
  first_number = input("\nFirst Number: ")
  if first_number == 'q':
    break
  second_number = input("Second Number: ")
  if second_number == 'q':
    break
  
  try:
    answer = float(first_number) / float(second_number)
  except ZeroDivisionError:
    print("You can't divide by 0!")
  else:
    print(answer)

# We ask Python to try to complete the division operation in a 'try' block (line 16), which includes the only code that might cause an error. Any code that depends on the 'try' block succeeding is added to the 'else' block. In this case if the division operation is successful, we use the 'else' block to print the result (line 20).

# The 'except' block tells Python how to respond when the 'ZeroDivisionError' arises (Line 18). If the 'try' block doesn't succeed because of a division by zero error, we print a friendly message telling the user how to avoid this kind of error. The program continues to run, and the user never sees a traceback.

# The 'try-except' block works like this: Python attempts to run the code in the 'try' block. The only code that should go in a 'try' block is code that might cause an exception to be raised. Sometimes you'll have additional code that should run only if the try block was successful; this code goes in the 'else' block. The 'except' block tells Python what to do in case a certain exception arises when it tries to run the code in the 'try' block.

# By anticipating likely sources of errors, you can write robust programs that continue to run even when they encounter invalid data and missing resources. Your code will be resistant to innocent user mistakes and malicious attacks.