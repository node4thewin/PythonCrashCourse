# IF-ELSE STATEMENTS

# Often, you'll want to take one action when a conditional test passes and a different action in all other cases. Python's if-else syntax makes this possible. An 'if-else' block is similar to a simple 'if' statement, but the 'else' statement allows you to define an action or set of actions that are executed when the conditional test fails.

# We'll display the same message we had previously if the person is old enough to vote, but this time we'll add a message for anyone who is not old enough to vote:

age = 17
if age >= 18:
  print("You are old enough to vote!")
  print("Have you registered to vote yet?")
else:
  print("Sorry, you are too young to vote.")
  print("Please register to vote as soon as you turn 18!")

# This code works because it has only two possible situations to evaluate: a person is either old enough to vote or not old enough to vote. The 'if-else' structure works well in situations in which you want Python to always execute one of two possible actions. In a simple 'if-else' chain like this, one of the two actions will always be executed.