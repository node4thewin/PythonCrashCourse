# 6-3 GLOSSARY

# A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let's call it a glossary.

# Think of five programming words you've learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.

# Print each word and its meaning as neatly formatted output. You might print the word followed by a colon an then its meaning, or print the word on one line and then print its meaning, or print the word on one line and then print its meaning indented on a second line. use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

glossary = {
  'print': "the output of whatever we want",
  'dictionaries': 'stores information of any data type',
  'list': 'stores values in a sequential form, can be integers or characters',
}

print_def = glossary['print'].title()
dictionaries = glossary['dictionaries'].title()
list_def = glossary['list'].title()

print(f"Print:  \n{print_def}")
print(f"\nDictionaries:  \n{dictionaries}")
print(f"\nList:  \n{list_def}")

# CORRECT VERSION (or related to Solutions Website)
glossary = {
  'print': "the output of whatever we want",
  'dictionaries': 'stores information of any data type',
  'list': 'stores values in a sequential form, can be integers or characters',
}

word = glossary['print'].title()
print(f"\nPrint:  \n{word}.")

word = glossary['dictionaries'].title()
print(f"\nDictionaries:  \n{word}.")

word = glossary['list'].title()
print(f"\nLists:  \n{word}.")

