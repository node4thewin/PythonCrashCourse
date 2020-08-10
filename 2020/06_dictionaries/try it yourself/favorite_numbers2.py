# 6-10 FAVORITE NUMBERS PART II

# Modify your program from Exercise 6-2 (page 99) so each person can have more than one favorite number. Then print each person's name along with their favorite numbers.

favorite_numbers = {
  'andrew': [14, 7, 20],
  'callie': [6, 16],
  'michael': [8, 2],
  'erika': [7, 21],
  'christian': [16, 14],
  'phil': [2, 8]
}

for person, numbers in favorite_numbers.items():
  numbers.sort() # added to see if it would sort integers
  print(f"\n{person.title()}'s favorite numbers are:")
  for number in numbers:
    print(f"  {number}")