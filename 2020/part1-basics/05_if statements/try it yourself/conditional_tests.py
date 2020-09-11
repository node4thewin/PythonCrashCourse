# 5-1 CONDITIONAL TESTS

# Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test. Your code should look something like this:

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# Look closely at your results, and make sure you understand why each line evaluates TRUE or FALSE.

# Create at least ten tests. Have at least five tests evaluate TRUE and another five that evaluate to FALSE.

print("\n\tTest One")
favorite_pizza = 'pepperoni'
print("\nIs my favorite_pizza == 'pepperoni'? I predict True.")
print(favorite_pizza == 'pepperoni')

print("\n\tTest Two")
old_car = 'subaru'
print("\nIs my old_car == 'subaru'? I predict True.")
print(old_car == 'subaru')

print("\n\tTest Three")
new_car = 'bronco'
print("\nWill my new_car == 'bronco'? I predict True.")
print(new_car == 'bronco')

print("\n\tTest Four")
callie = 'naked'
print("\nIs callie == 'naked'? I predict True.")
print(callie == 'naked')

print("\n\tTest Five")
otis = 'pug'
print("\nIs otis != 'german shephard'? I predict True.")
print(otis != 'german shephard')

print("\n\tTest Six")
callie = 'lovely'
print("\nIs callie == 'mean'? I predict False. She is lovely.")
print(callie == 'mean')

print("\n\tTest Seven")
otis = 'pug'
print("\nIs Otis a chihuahua? I think False. He is a Pug.")
print(otis == 'chihuahua')

print("\n\tTest Eight")
callie = 'clothed'
print("\nIs Callie still 'naked'? I think False, she has clothes on.")
print(callie == 'naked')

print("\n\tTest Nine")
current_favorite_car = 'bronco sport'
print("\nIs my favorite car still a 'jeep'? False, right now I want a Bronco.")
print(current_favorite_car == 'jeep')

print("\n\tTest Ten")
next_job = 'technical'
print("\nWill my next job be recruiting? I think False. I want to be technical.")
print(next_job == 'recruiting')

# 5-2 More Conditional Tests

# Tests for equality or inequality with strings

# Equality
print('\n\tTest for "Equality"\n')
callie = 'love'
print("Do I love Callie?")
print(f"That's obviously {callie == 'love'}.")

# Inequality
print('\n\tTest for "Inequality"\n')
print("Do I hate Callie?")
print(f"That's obviously {callie != 'love'}.")

# Test using the lower() method
new_user = 'nOde4tHeWiN'
user = 'node4thewin'

print('\n\tTest for "lower()" Method\n')
print('Has the username "nOde4tHeWiN" been used?')
if (new_user.lower() == user.lower()):
  print("Unfortunately that name has been taken.")
else:
  print("Welcome to the club!")

# Numerical tests involving equality or inequality, greater than and less than, greater than or equal to, and less than or equal to

print('\n\tNumerical Tests')
print('\nEquality and Inquality')
print('Is it true that 22 == 22?')
print(22 == 22)
print('\nIs it true that 22 != 23?')
print(22 != 23)

# Tests using the 'and' keyword and the 'or' keyword
print("\n\tTest using 'and' Keyword")
age1 = 18
language = 'Spanish'

print("\nAre you allowed to be here? You must be 18 years or older and able to speak Spanish.")
if (age1 >= 18) and (language == 'Spanish'):
  print("\nUnderstood! Welcome to the Spanish Cigar Club!")

print("\n\tTest using 'or' Keyword")
years_experience = 5
degree = 'Y'

print("\nDoes the candidate have 10+ years of experience or 6+ years and a Bachelors degree?")

if (years_experience >= 10) or ((years_experience >= 6) and (degree == 'Y')):
  print("\nYes, the candidate qualifies for the job.")
else:
  print("\nNo, the candidate does not meet those qualifications.")

# Test whether an item is in a list

print("\n\tTest showing whether an item is in a list.")

users = [
  'bieberh0le69', 'mgharvest', 'ctrlshftejct', 'kdickerson703'
]
user = 'kDICKerson703'

print("\nHas kDICKerson703 already been used?")

if user.lower() in users:
  print(f"Sorry {user} or another variation of it has already been used. Try again.")

# Test whether an item is not in a list
print("\n\tTest showing whether an item 'is not' in a list.")
print("\nHas kdick3rson703 been used?")
user = 'kdick3rson703'

if user.lower() not in users:
  print(f"Congratulations! That username has not been used. Welcome!")
