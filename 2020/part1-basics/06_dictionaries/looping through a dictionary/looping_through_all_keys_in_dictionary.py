# LOOPING THROUGH ALL THE KEYS IN A DICTIONARY

# The keys() method is useful when you don't need to work with all of the values in a dictionary. Let's loop through the 'favorite_languages' dictionary and print the names of everyone who took the poll:

favorite_languages = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'ruby',
  'phil': 'python',
}

for name in favorite_languages.keys():
  print(name.title())

# Looping through keys is actually the default behavior when looping throuhg a dictionary, so this code would have exactly the same output if you wrote:

for name in favorite_languages:
  print(name.title())

# You can choose to use the keys() method explicitly if it makes your code easier to read, or you can omit it if you wish.

# You can access the value associated with an key you care about inside the loop by using the current key. Let's print a message to a couple of friends about the languages they chose. We'll loop through the names in the dictionary as we did previously, but when the name matches one of our friends, we'll display a message about their favorite language:

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
  print(f"Hi {name.title()}.")

  if name in friends:
    language = favorite_languages[name].title()
    print(f"\t{name.title()}, I see you love {language}!")

# At line 24 we make a list of friends that we want to print a message to. Inside the loop, we print each person's name. Then at line 28 we check whether the 'name' we're working with is in the list of 'friends'. If it is, we determine the person's favorite language using the name of the dictionary and the current value of 'name' as the key (line 29). We then print a special greeting, including a reference to their language of choice.

# Everyone's name should be printed, but our friends receive a special message.

# You can also use the keys() method to find out if a particular person was polled. This time, let's find out if Erin took the poll:

if 'erin' not in favorite_languages.keys():
  print("\nErin, please take our poll!")