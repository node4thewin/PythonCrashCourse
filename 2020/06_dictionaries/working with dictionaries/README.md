# WORKING WITH DICTIONARIES

A 'dictionary' in Python is a collection of 'key-value pairs'. Each 'key' is connected to a value, and you can use a key to access the value associated with that key. A key's value can be a number, a string, a list, or even another dictionary. In fact, you can use any object that you can create in Python as a value in a dictionary. 

In Python, a dictionary is wrapped in braces, {}, with a series of 'key-value pairs' inside the braces, as shown in the earlier example:

alien_0 = {'color': 'green', 'points': 5}

A 'key-value pair' is a set of values associated with each other. when you provide a key, Python returns the value associated with that key. Every key is connected to its value by a colon, and individual key-value pairs are separated by commas. You can store as many key-value pairs as you want in a dictionary.

The simplest dictionary has exactly one key-value pair, as shown in this modified version of the alien_0 dictionary:

alien_0 = {'color': 'green'}

This dictionary stores one piece of information about 'alien_0', namely the alien's color. The string 'color' is a key in this dictionary, and its associated value is 'green'.