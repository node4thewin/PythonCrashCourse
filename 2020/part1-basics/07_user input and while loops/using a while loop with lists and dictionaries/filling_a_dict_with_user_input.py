# FILLING A DICTIONARY WITH USER INPUT

# You can prompt for as much input as you need in each pass through a 'while' loop. Let's make a polling program in which each pass through the loop prompts for the participant's name and response. We'll store the data we gather in a dictionary, because we want to connect each response with a particular user:

# Empty dictionary
responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
  # Prompt for the person's name and response.
  name = input("\nWhat's your name? ")
  response = input("Which mountain would you like to climb someday? ")

  # Store the response in the dictionary.
  responses[name] = response

  # Find out if anyone else is going to take the poll.
  repeat = input("Would you like to let another person respond? (y/n) ")
  if repeat == 'n':
    polling_active = False
  elif repeat == 'no':
    polling_active = False
  else:
    polling_active = True
  
# Polling is complete. Show the results
print("\n--- Poll Results ---")
for name, response in responses.items():
  print(f"{name} would like to climb {response}.")

# The program first defines an empty dictionary (responses) and sets a flag (polling_active) to indicate that polling is 'active'. As long as 'polling_active' is True, Python will run the code in the 'while' loop.

# Within the loop, the user is prompted to enter their name and a mountain they'd like to climb (line 12). That information is stored in the 'responses' dictionary (line 17), and the user is asked whether or not to keep the poll running (line 20). If they enter yes, the program enters the 'while' loop again. If they enter 'n' or 'no', the program enters the 'while' loop again. If they enter 'no', the 'polling_active' flag is set to 'False', the 'while' loop stops running, and the final code block at line 30 displays the results of the poll.