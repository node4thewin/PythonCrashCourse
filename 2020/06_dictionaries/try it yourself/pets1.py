pets = []

pet = {
  'name': 'otis',
  'owner': 'callie',
  'breed': 'pug'
}
pets.append(pet)

pet = {
  'name': 'lola',
  'owner': 'andrew',
  'breed': 'golden retriever'
}
pets.append(pet)

pet = {
  'name': 'ruth',
  'owner': 'penny',
  'breed': 'labrador retriever'
}
pets.append(pet)

pet = {
  'name': 'apollo',
  'owner': 'daniel',
  'breed': 'german shephard'
}
pets.append(pet)

pet = {
  'name': 'spencer',
  'owner': 'james',
  'breed': 'springer spaniel'
}
pets.append(pet)

pet = {
  'name': 'chai',
  'owner': 'xenia',
  'breed': 'mini golden doodle'
}
pets.append(pet)

pet = {
  'name': 'emma',
  'owner': 'erika',
  'breed': 'mix'
}
pets.append(pet)

pet = {
  'name': 'zorro',
  'owner': 'mike sr.',
  'breed': 'shih-tzu'
}
pets.append(pet)

pet = {
  'name': 'hesh',
  'owner': 'mike sr.',
  'breed': 'miniature schnauzer'
}
pets.append(pet)

pet = {
  'name': 'joey',
  'owner': 'susan',
  'breed': 'mini shih-tzu'
}
pets.append(pet)

for pet in pets:
  name = f"{pet['name'].title()}"
  owner = f"{pet['owner'].title()}"
  breed = f"{pet['breed'].title()}"

  print(f"{name} is a {breed} owned by {owner}!\n")
