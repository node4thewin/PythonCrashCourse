# A DICTIONARY OF SIMILAR OBJECTS

# Take note the organization/syntax for storing these dictionaries

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print(favorite_languages)

# To use this dictionary, given the name of a person who took the poll,
# you can easily look up their favorite language:

favorite_languages = {
    'andrew': 'python',
    'dad': 'c',
    'mom': 'ruby',
    'james': 'python',
    'penny': 'angular',
}

language = favorite_languages['andrew'].title()
print(f"Andrew's favorite language is {language}.")

# Doing it like above allows for a much cleaner print call.

