# PART II - LIST OF DICTIONARIES

# How might you work with a group of aliens like this? Imagine that one aspect of a game has some aliens changing color and moving faster as the game progresses. When it's time to change colors, we can use a 'for' loop and an 'if' statement to change the color of aliens. For example, to change the first three aliens to yellow, medium-speed aliens worth 10 points each, we could do this:

# blank list of aliens
aliens = []

# make 30 aliens
for alien_number in range(30):
  new_alien = {'color': 'green', 'points': '5', 'speed': 'slow'}
  aliens.append(new_alien)

# change first three aliens to yellow, 10 points, medium speed
for alien in aliens[:3]:
  if alien['color'] == 'green':
    alien['color'] = 'yellow'
    alien['points'] = '10'
    alien['speed'] = 'medium'

# show first 5 aliens
for alien in aliens[:5]:
  print(alien)
print("...")

# Because we want to modify the first three aliens, we loop through a 'slice' (remember from earlier chapters) that includes only the first three aliens. All of the aliens are gree nnow but that won't always be the case, so we write an 'if' statement to make sure we're only modifying green aliens. If the alien is green, we change the color to 'yellow', the speed to 'medium', and the point value to '10', as shown in the output.

# This could be expanded by adding an 'elif' block that turns yellow aliens into red, fast moving ones worth 15 points each. Without showing the entire program again, go to 'list_of_dictionaries3.py'