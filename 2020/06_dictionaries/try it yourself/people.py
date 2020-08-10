# 6-7 PEOPLE

# Start with the program you wrote for Exercise 6-1 (page 99). Make two new dictionaries representing different people, and store all three dictionaries in a list called 'people'. Loop through your list of people. As you loop through the list, print everything you know about each person.

# I adjusted people to usernames...you can see the solution at the bottom of this program.

usernames = {
  'biebrh0le69': {
    'first': 'callie',
    'last': 'barron',
    'relationship': 'girlfriend',
    'age': '27',
    'location': 'herndon',
  },
  'mgharvest': {
    'first': 'michael',
    'last': 'harvey',
    'relationship': 'brother',
    'age': '27',
    'location': 'sterling',
  },
  'mischiefmngd': {
    'first': 'erika',
    'last': 'gerard',
    'relationship': 'sister',
    'age': '31',
    'location': 'purcellville',
  },

}

for username, username_info in usernames.items():
  print(f"\nUsername: {username}")
  full_name = f"{username_info['first']} {username_info['last']}"
  relation = username_info['relationship']
  age = username_info['age']
  location = username_info['location']

  print(f"\tFull name: {full_name.title()}")
  print(f"\tRelation: {relation.title()}")
  print(f"\tAge: {age.title()}")
  print(f"\tLocation: {location.title()}")

# this is the version from SOLUTIONS:

people = []

person = {
  'first_name': 'eric',
  'last_name': 'matthes',
  'age': 46,
  'city': 'sitka',
}
people.append(person)

person = {
  'first_name': 'lemmy',
  'last_name': 'matthes',
  'age': 2,
  'city': 'sitka',
}
people.append(person)

person = {
  'first_name': 'willie',
  'last_name': 'matthes',
  'age': 11,
  'city': 'sitka',
}
people.append(person)

# Display all of the information in the dictionary.
for person in people:
  name = f"{person['first_name'].title()} {person['last_name'].title()}"
  age = person['age']
  city = person['city'].title()

  print(f"{name}, of {city}, is {age} years old.")
  # make sure this print() call is a part of the for loop.
