# A LIST IN A DICTIONARY

# Rather than putting a dictionary inside a list, it's sometimes useful to put a list inside a dictionary. For example, consider how you might describe a pizza that someone is ordering. if you were to use only a list, all you could really store is a list of the pizza's toppings. With a dictionary, a list of toppings can be just one aspect of the pizza you're describing.

# In the following example, two kinds of information are stored for each pizza: a type of crust and a list of toppings. The list of toppings is a value associated with the key 'toppings'. To use the items in the list, we give the name of the dictionary and the key 'toppings', as we would any value in the dictionary. Instead of returning a single value, we get a list of toppings:

# Store information about a pizza being ordered:
pizza = {
  'crust': 'thick',
  'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize the order.
print(f"You ordered a {pizza['crust'].title()}-crust Pizza "
  "with the following toppings:")

for topping in pizza['toppings']:
  print("\t" + topping.title())

# We begin at line 8 with a dictionary that holds information about a pizza that has been ordered. One key in the dictionary is 'crust', and the associated value is the string 'thick'. The next key, 'toppings', has a list as its value that stores all requested toppings. At line 14 we summarize the order before building the pizza. When you need to break up a long line in a print() call, choose an appropriate point at which to break the line being printed, and end the line with a quotation mark. Indent the next line, add an opening quotation mark, and continue the string. Python will automatically combine all of the strings it finds inside the parentheses. To print the toppings, we write a 'for' loop (line 17). To access the list of toppings, we use the key 'toppings', and Python grabs the list of toppings from the dictionary.

# You can nest a list inside a dictionary any time you want more than one value to be associated with a single key in a dictionary. In the earlier example of favorite programming languages, if we were to store each person's response in a list, people could choose more than one favorite language. When we loop through the dictionary, the value associated with each peron would be a list of languages rather than a single language. Inside the dictionary's 'for' loop, we use another 'for' loop to run through the list of lanuages associated with each person:

print("\n\tFavorite Languages Example:")

favorite_languages = {
  'jen': ['python', 'ruby'],
  'sarah': ['c'],
  'edward': ['ruby', 'go'],
  'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
  print(f"\n{name.title()}'s favorite languages are:")
  for language in languages:
    print(f"\t{language.title()}")

# As you can see at line 16 the value associated with each name is now a list. Notice that some people have one favorite language and others have multiple favorites. When we loop through the dictionary at line 33, we use the variable name 'languages' to hold each value from the dictionary, because we know that each value will be a list. Inside the main dictionary loop, we use another 'for' loop to run through each person's list. Inside the main dictionary loop, we use another 'for' loop (line 35) to run through each person's list of favorite languages. Now each person can list as many favorite languages as they like.

# To refine this program even further, you could include an 'if' statement at the beginning of the dictionary's 'for' loop to see whether each person has more than one favorite language by examining the value of 'len(languages)'. if a person has more than one favorite, the output would stay the same. If the person has only one favorite language, you could change the wording to reflect that. For example, you could say "Sarah's favorite language is C."

# NOTE - You should not nest lists and dictionaries too deeply. If you're nesting items much deeper than what you see in the preceding examples or you're working with someone else's code with significant levels of nesting, most likely a simpler way to solve the program exists.