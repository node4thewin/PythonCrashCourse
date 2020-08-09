# 7-5 MOVIE TICKETS

# A movie theater charges different ticket prices depending on a person's age. If a person is under the age of 3, the ticket is free; if they are between the ages of 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.

prompt = "How old are you? "
prompt += "(Type 'quit' at anytime to leave program.) "

age = ""
while True:
  age = input(prompt)
  if age == 'quit':
    break # must put the flag before age turns into an 'int' if it's an integer, and 'quit' is a string...it won't work
  age = int(age)

  if age < 3:
    print("Your ticket is free!")

  elif age >= 3 and age < 12:
    print("Your ticket costs $10.")
  
  else:
    print("Your ticket costs $15.")