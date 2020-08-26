# RETURNING A DICTIONARY

# A function can return any kind of value you need it to, including more complicated data structures like lists and dictionaries. For example, the following function takes in parts of a name and returns a dictionary representing a person:

# def build_person(first_name, last_name):
#   """Return a dictionary of information about a person"""
#   person = {'first': first_name, 'last': last_name}
#   return person

# musician = build_person('jimi', 'hendrix')
# print(musician)

# The function 'build_person()' takes in a first and last name, and puts these values into a dictionary at line 7. The value 'first_name' is stored with the key 'first', and the value of 'last_name' is stored with the key 'last'. The entire dictionary representing the person is returned at line 8. The return value is printed at line 11 with the original two pieces of textual information now stored in a dictionary.

# This function takes in simple textual information and puts it into a more meaningful data structure that lets you work with the information beyond just printing it. THe strings 'jimi' and 'hendrix' are now labeled as a first name and last name. You can easily extend this function to accept optional values like a middle name, an age, an occupation, or any other information you want to store about a person. For example, the following change allows you to store a person's age as well:

def build_person(first_name, last_name, age=None): # None is a placeholder value, and always evaluates to False
  """Return a dictionary of information about a person."""
  person = {'first': first_name, 'last': last_name} # this is the dictionary
  if age:
    person['age'] = age
  return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

# We add a new optional parameter 'age' to the function definition and assign the parameter the special value 'None', which is used when a variable has not specific value assigned to it. You can think of 'None' as a placeholder value. In conditional tests, 'None' evaluates to 'False'. If the function call includes a value for 'age', that value is stored in the dictionary. This function always stores a person's name, but it can also be modified to store any other information you want about a person.