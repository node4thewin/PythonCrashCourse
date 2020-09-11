# 6-8 PETS

# Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner's name. Store these dictionaries in a list called 'pets'. Next, loop through your list and as you do, print everything you know about each pet.

pets = []

pet = {
  'name': 'otis',
  'owner': 'callie',
  'breed': 'white pug',
}
pets.append(pet)

pet = {
  'name': 'spencer',
  'owner': 'james',
  'breed': 'white pug',
}
pets.append(pet)

pet = {
  'name': 'lola',
  'owner': 'andrew',
  'breed': 'golden retriever',
}
pets.append(pet)

pet = {
  'name': 'apollo',
  'owner': 'daniel gerard',
  'breed': 'german shephard',
}
pets.append(pet)

pet = {
  'name': 'emma',
  'owner': 'erika gerard',
  'breed': 'mix',
}
pets.append(pet)

pet = {
  'name': 'chai',
  'owner': 'xenia',
  'breed': 'mini golden doodle',
}
pets.append(pet)

for pet in pets:
  name = f"{pet['name'].title()}"
  age = f"{pet['owner']}"
  breed = f"{pet['breed']}"

