# 6-6 POLLING: Use the code in 'favorite_languages.py'

# Make a list of people who should take the favorite languages poll. Include some names that are already in the dictionary and some that are not.

# Loop through a list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding. If they have not yet taken the poll, print a message inviting them to take the poll.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
  print(f"{name.title()}'s favorite language is {language.title()}.")

developers = [
  'callie', 'jen', 'sarah', 'edward', 'andrew', 'phil', 'erika'
]

for developer in developers:
  if developer in favorite_languages.keys():
    print(f"Thanks for taking the poll {developer.title()}.")
  
  else:
    print(f"{developer.title()}, what's your favorite programming language?")
  
