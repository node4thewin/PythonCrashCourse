# 5-3 ALIEN COLORS #3

# Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.

# If the alien is green, print a message that the player earned 5 points.
# If the alien is yellow, print a message that the player earned 10 points.
# If the alien is red, print a message that the player earned 15 points.

# Write three versions of this program, making sure each message is printed for the appropriate color alien.

# VERSION ONE:
alien = 'green'

if alien == 'green':
  print(f"Killed {alien.title()} Alien! 5 Points Earned.\n")
elif alien == 'yellow':
  print(f"Killed {alien.title()} Alien! 10 Points Earned.\n")
else:
  print(f"Killed {alien.title()} Alien! 15 Points Earned.\n")

# VERSION TWO:
alien = 'yellow'

if alien == 'green':
  print(f"Killed {alien.title()} Alien! 5 Points Earned.\n")
elif alien == 'yellow':
  print(f"Killed {alien.title()} Alien! 10 Points Earned.\n")
else:
  print(f"Killed {alien.title()} Alien! 15 Points Earned.\n")

# VERSION THREE:
alien = 'red'

if alien == 'green':
  print(f"Killed {alien.title()} Alien! 5 Points Earned.\n")
elif alien == 'yellow':
  print(f"Killed {alien.title()} Alien! 10 Points Earned.\n")
else:
  print(f"Killed {alien.title()} Alien! 15 Points Earned.\n")