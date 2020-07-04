# CHECKING FOR EQUALITY

# Most conditional tests compare the current value of a variable to a specific value of interest. The simplest conditional test checks whether the value of a variable is equal to the value of interest:

car = 'bmw'
print(car=='bmw')

# The line at 5 sets the value of car to 'bmw' using a single equal sign, as you've seen many times already. The line at 6 checks whether the value of car is 'bmw' using a double equaly sign (==). This "equality operator" returns 'True' if the values on the left and right side of the operator match, and 'False' if they don't match. The values in this example match, so Python returns 'True'.

# When the value of a car is anything other than 'bmw' the test returns False:

print(car == 'subaru')

# A single equal sign is really a statement; you might read the code at line 5 as "Set the value of the car equal to 'bmw'. On the other hand, a double equal sign, like the one at line 12, asks a question: "Is the value of car equal to 'subaru'?" Most programming languages use equal signs this way.
