# 7-6 EXIT TWO

# Use an 'active' variable to control how long the loop runs.

prompt = "Type your age to find out ticket cost: "

active = True
while active:
  age = input(prompt)
  if age == 'quit':
    active = False
  
  if active == True:
    age = int(age)
    if age < 3:
      print("Your ticket is free!")

    elif age >= 3 and age < 12:
      print("Your ticket costs $10.")
  
    else:
      print("Your ticket costs $15.")