# USING A FLAG

# In the previous example, we had the program perform certain tasks while a given condition was true. But what about more complicated programs in which many different evens could cause the program to stop running?

# For example, in a game, several different events can end a game. When the player runs out of ships, their time runs out, or the cities they were supposed to protect were all destroyed, the game should end. It needs to end if anyone of these events happens. If many possible events might occur to stop the program, trying to test all these conditions in one 'while' statement becomes complicated and difficult.

# For a program that should run only as long as many conditions are true, you can define one variable that determines whether or not the ENTIRE program is active. This variable, called a 'flag', acts as a signal to the program. We can write our programs so they run while flag is set to 'True' and stop runnign when any of several events sets the value of the flag to 'False'. As a result, our overall 'while' statement needs to check only one condition: whether or not the flag is currently 'True'. Then, all our other tests (to see if an event has occurred that should set the flag to 'False') can be neatly organized in the rest of the program.

# Let's add a flag to the parrot program from the previous section. This flag, which we'll call 'active' (though you can call it anything), will monitor whether or not the program should continue running:

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True

while active:
  message = input(prompt)

  if message == 'quit':
    active = False
  else:
    print(message)