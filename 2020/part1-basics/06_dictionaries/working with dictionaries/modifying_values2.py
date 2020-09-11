# MODIFYING VALUES IN A DICTIONARY TWO

# For a more interesting example, let's track the position of an alien that can move at different speeds. We'll store a value representing the alien's current speed and then use it to determine how far to the right the alien should move:

alien_0 = {
  'x_position': 0, 'y_position': 25, 'speed': 'medium'
  }

print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
  x_increment = 1
elif alien_0['speed'] == 'medium':
  x_increment = 2
else:
  # This must be a fast alien.
  x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

# We start by defining an alien with an initial x position and y position, and a speed of 'medium'. We've omitted the color and point values for the sake of simplicity, but this example would work the same way if you included those key-value pairs as well. We also print the original value of x_position to see how far the alien moves to the right.

# At line 13, an 'if-elif-else' chain determines how far the alien should move to the right and assigns this value to the variable x_increment. If the alien's speed is 'slow', it moves one unit to the right; if the speed is 'medium', it moves two units to the right; and if it's 'fast', it moves three units to the right. Once the increment has been calculated, it's added to the value of x_position at line 22, and the result is stored in the dictionary's x_position.

# Because this is a medium-speed alien, its position shifts two units to the right. This technique is pretty cool: by changing one value in the alien's dictionary, you can change the overall behavior of the alien. For example, to turn this medium-speed alien into a fast alien, you would add the line:

alien_0['speed'] = 'fast' # this would have to be added before the print 'if-elif-else'