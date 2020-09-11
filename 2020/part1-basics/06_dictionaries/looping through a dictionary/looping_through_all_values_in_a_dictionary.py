# LOOPING THROUGH ALL VALUES IN A DICTIONARY

# If you are primarily interested in the values that a dictionary contains, you can use the 'values()' method to return a list of values without any keys. For example, say we simply want a list of all languages chosen in our programming language poll without the name of the person who chose each language:

favorite_languages = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'ruby',
  'phil': 'python',
}

print("The following languages have been mentioned:")
for language in favorite_languages.values():
  print(f"\t{language.title()}")

# The 'for' statement here pull each value from the dictionary and assigns it to the variable 'language'. When these values are printed, we get a list of all chosen languages.

# This approach pulls all the values from the dictionary without checking for repeats. That might work fine with a smalle number of values, but in a poll with a large number of respondents, this would result in a very repetitive list. To see each language chosen without repetition, we can use a 'set'. A 'set' is a collection in which each item must be unique:

favorite_languages = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'ruby',
  'phil': 'python',
}

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
  print(language.title())

# When you wrap 'set()' around a list that contains duplicate items, Python identifies the unique items in the list and build a set from those items. At line 28 we use 'set()' to pull out the unique languages in 'favorite_languages.value()'. The result is a nonrepetitive list of languages that have been mentioned by people taking the poll. As you continue learning about Python, you'll often find a built-in feature of the language that helps you do exactly waht you want with your data.

# NOTE - You can build a set directly using braces and separating the elements with commas:

# >>> languages = {'python', 'ruby', 'python', 'c'}
# >>> languages
# {'ruby', 'python', 'c'}

# It's easy to mistake sets for dictionaries because they're both wrapped in braces. When you see braces but no key-value pairs, you're probably looking at a set. Unlike lists and dictionaries, sets do not retain items in any specific order.