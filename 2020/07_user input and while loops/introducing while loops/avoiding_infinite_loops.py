# AVOIDING INFINITE LOOPS

# Every 'while' loop needs a way to stop running so it won't continue to run forever. For example, this counting loop should count from 1 to 5:

x = 1
while x <= 5:
  print(x)
  x += 1

# But if you accidentally omit the line x += 1 (as shown next), the loop will run forever:

# This loop runs forever!
x = 1
while x <= 5:
  print(x)

# If your program gets stuck in an infinite loop, press CTRL-C or just close the terminal window displaying your program's output.

# To avoid writing infinite loops, test every 'while' loop and make sure the loop stopes when you expect it to. If you want your program to end when the user enters a certain input value, run the program and enter that value. If the program doesn't end, scrutinize the way your program handles the value that should cause the loop to exit. Make sure at least one part of the program can make the loop's condition 'False' or cause it to reach a 'break' statement.