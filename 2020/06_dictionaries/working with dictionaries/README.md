# WORKING WITH DICTIONARIES

A 'dictionary' in Python is a collection of 'key-value pairs'. Each 'key' is connected to a value, and you can use a key to access the value associated with that key. A key's value can be a number, a string, a list, or even another dictionary. In fact, you can use any object that you can create in Python as a value in a dictionary. 

In Python, a dictionary is wrapped in braces, {}, with a series of 'key-value pairs' inside the braces, as shown in the earlier example:

alien_0 = {'color': 'green', 'points': 5}

A 'key-value pair' is a set of values associated with each other. when you provide a key, Python returns the value associated with that key. Every key is connected to its value by a colon, and individual key-value pairs are separated by commas. You can store as many key-value pairs as you want in a dictionary.

The simplest dictionary has exactly one key-value pair, as shown in this modified version of the alien_0 dictionary:

alien_0 = {'color': 'green'}

This dictionary stores one piece of information about 'alien_0', namely the alien's color. The string 'color' is a key in this dictionary, and its associated value is 'green'.

#SUMMARY

In this chapter you learned how to define a dictionary and how to work with the information stored in a dictionary. You learned how to access and modify individual elements in a dictionary, and how to loop through all of the information in a dictionary. You learned to loop through a dictionary's key-value pairs, its keys, and its values. You also learned how to nest multiple dictionaries in a list, nest lists in a dictionary and nest a dictionary inside a dictionary.

In the next chapter you'll learn about 'while' loops and how to accept input from people who are using your programs. This will be an exciting chapter, because you'll learn to make all of your programs interactive: they'll be able to response to user input.