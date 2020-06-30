# Using Variables in Strings

# In some situations, you'll want to use a variable's value inside a string. For example, you might want two variables to represent a first name
# and a last name respectively, and then want to combine those values to display someone's full name:

first_name = 'ada'
last_name = 'lovelace'

# To insert a variable's value into a string, place the letter "f" immediately before the opening quotation mark. Put braces {} around the name
# or names of any vraibles you want to use inside the string. Python will replace each variable with its value when the string is displayed.

full_name = f'{first_name} {last_name}'
print(full_name)

# These strings are called "f-strings". The "f" is format, because Python formats the string by replacing the name of any variable in braces with its
# value. 

# You can do a lot with f-strings. For example, you can us f-strings to compose complete messages using the information associated with a variable,
# as seen below.

print(f'Hello, {full_name.lower()}!')
print(f'Hello, {full_name.title()}!')
print(f'Hello, {full_name.upper()}!')

# You can also use f-strings to compose a message, and then assign the entire message to a variable:

message = f'Hello, {full_name.title()}!'
print(message)

# ADDING WHITESPACE TO STRINGS WITH TABS OR NEWLINES
# In programming, whitespace refers to any nonprinting character, such as spaces, tabs, and end-of-line symbols. You can use whitespace to organize
# your output so it's easier for users to read.

print("Python")
print("\tPython")

# To add a newline in a string, use the character combination \n:

print("Languages:\nPython\n\C\nJavaScript\nAngular.js\nReact.js")




