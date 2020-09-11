# PART III - List of Dictionaries

# this shows adding the elif statement switching the aliens to red, fast moving, and 15 points if they are yellow.

# blank list of aliens
aliens = []

# make 30 aliens
for alien_number in range(30):
  new_alien = {'color': 'green', 'points': '5', 'speed': 'slow'}
  aliens.append(new_alien)

# change first three aliens to yellow, 10 points, medium speed
# afterwards, add elif statement changing yellow to red, 15, fast speed
for alien in aliens[0:3]:
  if alien['color'] == 'green':
    alien['color'] = 'yellow'
    alien['points'] = '10'
    alien['speed'] = 'medium'
  elif alien['color'] == 'yellow':
    alien['color'] = 'red'
    alien['points'] = '15'
    alien['speed'] = 'fast'

# show first 5 aliens
for alien in aliens[:5]:
  print(alien)
print("...")