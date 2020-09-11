# CHECKING FOR INEQUALITY

# When you want to determine whether two values are not equal, you can combin an exclamation point and an equal sign (!=). The exclamation point represents 'not', as it does in many programming languages.

# Let's use another 'if' statement to examind how to use the inequality operator. We'll store a requested pizza topping in a variable and then print a message if the person did not order anchovies:

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
  print("HOLD THE ANCHOVIES PLEASE!!!")

# The line at 9 compares the value of 'requested_topping' to the value of 'anchovies'. If these two values do not match, Python returns 'True' and executes the code following the 'if' statement. If the two values match, Python returns 'False' and does not run the code following the 'if' statement.

# Because the value of 'requested_topping' is not 'anchovies', the print() function is executed.

# MOST OF THE CONDITIONAL EXPRESSIONS YOU RIGHT WILL TEST FOR EQUALITY, BUT SOMETIMES YOU'LL FIND IT MORE EFFICIENT TO TEST FOR INEQUALITY.
