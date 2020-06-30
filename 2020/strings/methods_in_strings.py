# VARIABLES

# Changing Case in a String with Methods
# One of the simplest tasks you can do with strings is change the case of teh words in a string. Look at the following code, and try to determine what's happening:

name = 'ada lovelace'
print(name.title())

# In this example, the variable "name" refers to the lowercase 'ada lovelace'. The method "title()" apears after the variable in the print() call. A "method" is an
# action that Python can perform on a piece of data. The dot (.) tells Python to make the title() method act on the variable "name". Every method is followed by a
# set of parentheses. The title() function doesn't need any additional information, so it's parentheses are empty.
# 
# The title() method changes each word to title case, where each word begins with a capital letter. This is useful because you'll often want to think of a name as
# a piece of information. For example, you might want to program to recognize the input values Ada, ADA, and ada as the same name, and display all of them as Ada.

# There are several other useful methods for dealing with case as well. For example, you can change a string to all uppercase or all lowercase letters like this:

name = 'Ada Lovelace'
print(name.upper())
print(name.lower())

# The lower() method is useful for storing data. You may not trust the capitalization that your users provide, so you'll convert strings to lowercase before storing
# them. 