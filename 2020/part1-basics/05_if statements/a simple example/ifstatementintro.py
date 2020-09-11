# A SIMPLE EXAMPLE

# The following short example shows how 'if' tests let you respond to special situations correctly. Imagine you have a list of cars and you want to print out the name of each car. Car names are proper names, so the names of most cars should be printed in title case. However, the value 'bmw' should be printed in all uppercase. The following code loops through a list of car names and looks for the value 'bmw'. Whenever the value is 'bmw', it's printed in uppercase instead of title case.

cars = ['audi', 'bmw', 'subaru', 'toyota', 'ford']

for car in cars:
  if car == 'bmw':
    print(car.upper())
  else:
    print(car.title())

# The loop in this example first checks if the current value of car is 'bmw'. If it is, the value is printed in uppercase. If the value of car is anything other than 'bmw', it's printed in title case.

# This example combines a number of the concepts you'll learn about in this chapter. Let's begin by looking at the kinds of tests you can use to examin the conditions in your program.

