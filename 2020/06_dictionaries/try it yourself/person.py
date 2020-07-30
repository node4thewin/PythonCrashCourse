# 6-1 PERSON

# Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as 'first_name', 'last_name', 'age', 'city'. Print each piece of information stored in your dictionary.

person = {
  'first_name': 'callie',
  'last_name': 'barron',
  'relationship': 'girlfriend',
  'age': '27',
  'city': 'herndon'
  }

first_name = person['first_name'].title()
print(f"The person's first name is {first_name}.\n")

last_name = person['last_name'].title()
print(f"The person's last name is {last_name}.\n")

relationship = person['relationship'].title()
print(f"The person's relationship to me is {relationship}.\n")

age = person['age'].title()
print(f"The person's age is {age}.\n")

city = person['city'].title()
print(f"I met this person in {city}.\n")

