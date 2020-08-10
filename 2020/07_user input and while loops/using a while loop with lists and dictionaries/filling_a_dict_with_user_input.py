# FILLING A DICTIONARY WITH USER INPUT

# You can prompt for as much input as you need in each pass through a 'while' loop. Let's make a polling program in which each pass through the loop prompts for the participant's name and response. We'll store the data we gather in a dictionary, because we want to connect each response with a particular user:

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