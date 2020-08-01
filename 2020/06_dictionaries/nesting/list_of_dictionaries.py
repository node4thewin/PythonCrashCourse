# A LIST OF DICTIONARIES

# The 'alien_0' dictionary contains a variety of information about one alien, but it has no room to store information about a second alien, much less a screen full of aliens. How can you manage a fleet of aliens? One way is to make a list of aliens in which each alien is a dictionary of information about that alien. For example, the following code builds a list of three aliens:

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
  print(alien)

# We first create three dictionaries, each representing a different alien. At line 9 we store each of these dictionaries in a list called 'aliens'. Finally we loop through the list and print out each alien.

# A more realistic example would involve more than three aliens with code that automatically generates each alien. In the following example we use 'range()' to create a fleet of 30 aliens:

# # Make an empty list for storing aliens.
# aliens = []
# print("...")

# # Make 30 green aliens.
# for alien_number in range(30):
#   new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#   aliens.append(new_alien)

# # Show the first 5 aliens.
# for alien in aliens[:5]:
#   print(alien)
# print("...")

# # Show how many aliens have been created.
# print(f"Total number of aliens: {len(aliens)}")

# This example begins with an empty list to hold all of the aliens that will be created. At line 23 range() returns a series of numbers, which just tells Python how many times we want the loop to repeat. Each time the loop runs we create a new alien to the list 'aliens' at line 24. At line 28 we use a slice to print the first five aliens, and then at line 33 we print the length of the list to prove we've actually generated the full fleet of 30 aliens.

# These aliens all have the same characteristics, but Python considers each one a separate object, which allows us to modify each alien individually.

# How might you work with a group of aliens like this? Imagine that one aspect of a game has some aliens changing color and moving faster as the game progresses. When it's time to change colors, we can use a 'for' loop and an 'if' statement to change the color of aliens. For example, to change the first three aliens to yellow, medium-speed aliens worth 10 points each, we could do this:

aliens = []
print("...")

# Make 30 green aliens.
for alien_number in range(30):
  new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
  aliens.append(new_alien)

for alien in aliens[:3]:
  if alien['color'] == 'green':
    alien['color'] == 'yellow'
    alien['speed'] == 'medium'
    alien['points'] == '10'

# Show the first 5 aliens.
for alien in aliens[:5]:
  print(alien)
print("...")