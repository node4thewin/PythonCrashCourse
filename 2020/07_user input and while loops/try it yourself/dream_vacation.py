# 7-10 DREAM VACATION

# Write a program that polls user about their dream vacation. Write a prompt similar to "If you could visit one place in the world, where would you go?". Include a block of code that prints the results of the poll.

results = {}

questionnaire_active = True

while questionnaire_active:
  name = input("\nWhat's your name? ")
  location = input("\nWhere would your dream vacation be? ")
  
  # need to store the responses in the dictionary
  results[name] = location

  # Find out if there is any other dream vacation spots
  repeat = input("Would you like to let someone else respond? (y/n) ")
  
  if repeat == 'yes':
    questionnaire_active = True
  elif repeat != 'y':
    questionnaire_active = False
  
  # THIS WAS BEFORE I REFINED IT ABOVE
  # if repeat == 'n':
  #   questionnaire_active = False
  # elif repeat == 'no':
  #   questionnaire_active = False
  # else:
  #   questionnaire_active = True

print("\n--- SUMMARY --- \n")
for name, location in results.items():
  print(f"{name.title()} would like to go to {location.title()}.")