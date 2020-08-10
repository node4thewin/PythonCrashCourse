# THE 'while' LOOP IN ACTION

# You can use a 'while loop to count up through a series of numbers. For example, the following 'while' loop counts from 1 to 5:

current_number = 1
while current_number <= 5:
  print(current_number)
  current_number += 1

# In the first line, we start counting from 1 by assigning 'current_number' the value 1. The 'while' loop is then set to keep running as long as the value of 'current_number' is less than or equal to 5. The code inside the loop prints the value of 'current_number' and then adds 1 to that value with 'current_number += 1'.

# The += operator is shorthand for current_number = current_number + 1.

# Python repeats the loop as long as the condition 'current_number <= 5 is true. Because 1 is less than 5, Python prints 1 and then adds 1, making the current number 2. Because 2 is less than 5, Python prints 2 and then adds 1 again, making the current number 3, and so on. Once the value of 'current_number' is greater than 5, the loop stops running and the program ends.

# The programs you use everyday most likely contain 'while' loops. For example, a game needs a 'while' loop to keep running as long as you want to keep playing, and so it can stop runnign as soon as you ask it to quit. Programs wouldn't be fun to use if they stopped running before we told them to or kept running even after we wanted to quit, so 'while' loops are quite useful.

