# LOOPING THROUGH A DICTIONARY'S KEYS IN A PARTICULAR ORDER

# Starting in Python 3.7, looping through a dictionary returns the items in the same order they were inserted. Sometimes though, you'll want to loop through a dictionary in a particular order.

# Only way to do this is to sort the keys as they're returned in the 'for' loop. You can use the 'sorted()' function to get a copy of the keys in order:

favorite_languages = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'ruby',
  'phil': 'python',
}

for name in sorted(favorite_languages.keys()):
  print(f"{name.title()}, thank you for taking the poll.")

# This 'for' statement is like other 'for' statements except that we've wrapped the sorted() function around the dictionary.keys() method. This tells Python to list all keys in the dictionary and sort that list before looping through it. The output shows everyone who took the poll, with the names displayed in order.
