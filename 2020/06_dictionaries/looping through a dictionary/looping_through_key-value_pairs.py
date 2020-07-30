# LOOPING THROUGH ALL KEY-VALUE PAIRS

# Before we explore the different approaches to looping, let's consider a new dictionary designed to store information about a user on a website. The following dictionary would store one person's username, first name, and last name:

user_0 = {
  'username': 'efermi',
  'first': 'enrico',
  'last': 'fermi',
}

# You can access any single piece of information about user_0 based on what you've already learned in this chapter. But what if you wanted to see everything stored in this user's dictionary? To do so, you could loop through the dictionary using a 'for' loop:

for key, value in user_0.items():
  print(f"\nKey: {key}")
  print(f"Value: {value}")

# As shown at line 13, to write a 'for' loop for a dictionary, you create names for the two variable that will hold the key and value in each key-value pair. You can choose any names you want for these two variables. This code would work just as well if you had used abbreviations for the variable names, like this:

for k, v in user_0.items():
  print(f"\nKey: {k}")
  print(f"Value: {v}")

# The second half of the 'for' statement at line 19 includes the name of the dictionary followed by the method 'items()', which returns a list of key-value pairs (REMEMBER THIS). The 'for' loop then assigns each of these pairs to the two variables provided. In the preceding example, we use the variables to print each 'key' (line 14), followed by the associated 'value' (line 15). The "\n" in the first print() call ensures that a blank line is inserted before each key-value pair in the output:

print("\n")

# Looping through all key-value pairs works particularly well for dictionaries like the 'favorite_languages.py' example on page 97, which stores the same kind of information for many different keys. If you loop through the 'favorite_languages' dictionary, you get the name of each person in the dictionary and their favorite programming language. Because the keys always refer to a person's name and the value is always a language, we'll use the variables 'name' and 'language' in the loop instead of 'key' and 'value' like above. This will make it easier to follow what's happening inside the loop:

favorite_languages = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'ruby',
  'phil': 'python',
}

for name, language in favorite_languages.items():
  print(f"{name.title()}'s favorite language is {language.title()}.")

