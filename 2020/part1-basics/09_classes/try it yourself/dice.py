# 9-13 Dice

# Make a class 'Die' with one attribute called 'sides', which has a default value of 6. Write a method called 'roll_die()' that prints a random number between 1 and the number of sides the die has. Make a 6-sided die and roll it 10 times.

# Make a 10-sided die and a 20-sided die. Roll each die 10 times.
from random import randint

class Die:
  """print random number to represent rolling a dice."""

  def __init__(self, sides=6):
    """Initialize a die with default of 6 sides."""
    self.sides = sides

  def roll_die(self):
    """Display a random number to signify rolling the dice."""
    return randint(1, self.sides)
  
# 6-sided die, with results
d6 = Die()

results = []
for roll_num in range(10):
  result = d6.roll_die()
  results.append(result)
print("\n10 rolls of a 6-sided die:")
print(results)

# 10-sided die, with results
d10 = Die(sides=10)

results = []
for roll_num in range(10):
  result = d10.roll_die()
  results.append(result)
print("\n10 rolls of a 10-sided die:")
print(results)

# 20-sided die, with results
d20 = Die(sides=10)

results = []
for roll_num in range(10):
  result = d20.roll_die()
  results.append(result)
print("\n10 rolls of a 20-sided die:")
print(results)
