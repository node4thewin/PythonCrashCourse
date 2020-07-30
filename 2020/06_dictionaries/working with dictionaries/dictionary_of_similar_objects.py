# A DICTIONARY OF SMALL OBJECTS

# The previous example involved storing different kinds of information about one object, an alien in a game. You can use a dictionary to store one kind of information about many objects. For example, say you want to poll a number of peopleand ask them what their favorite programming language is. A dictionary is useful for storing the results of a simple poll, like this:

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

# As you can see, we've broken a larger dictionary into several lines. Each key is the name of a person who responded to the poll, and each value is their language choice. When you know you'll need more than one line to define a dictionary, press ENTER after opening the brace. Then indent the next line one level (four spaces or two depending on your settings), and write the first key-value pair, followed by a comma. From this point forward when you press ENTER, your text editor should automatically indent all subsequent key-value pairs to match the first key-value pair.

# Once you've finished defining the dictionary, ass a closing brace on a new line after the last key-value pair and indent it one level so it aligns with the keys in the dictionary. It's good practice to include a comma after the last key-value pair as well, so you're ready to add a new key-value pair on the next line.

# NOTE - Most editors have some functionality that helps you format extended lists and dictionaries in a similar manner to this example. Other acceptable ways to format long dictionaries are available as well, so you may see slightly different formatting in your editor or in other sources.

# To use this dictionary, given the name of a person who took the poll, you can easily look up their favorite language:

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# We use the syntax to pull Sarah's favorite language from the dictionary at line 27 and assign it to the variable 'language'. Creating a new variable here makes for a much cleaner print() call. The output shows Sarah's favorite language. You could use this same syntax with any individual represented in the dictionary:

language = favorite_languages['jen'].title()
print(f"Jen's favorite language is {language}.")

language = favorite_languages['edward'].title()
print(f"Edward's favorite language is {language}.")

language = favorite_languages['phil'].title()
print(f"Phil's favorite language is {language}.")