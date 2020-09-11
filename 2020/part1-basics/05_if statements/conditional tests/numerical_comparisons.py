# NUMERICAL COMPARISONS

# Testing numerical values is pretty straightforward. For example, the following code checks whether a person is 18 years old:

age = 18
print(age == 18)

# You can also test to see if two numbers are not equal. For example, the following code pritns a message if the given answer is not correct:

answer = 17

if answer != 42:
  print("That is not the correct answer. Please mothafuckin' try again!")

# You can include various mathematical comparisons in your conditional statements as well, such as less than, less than or equal to, greater than, and greater than or equal to:

age = 19
print(age < 21) #less than
print(age <= 21) #less than or equal to
print(age > 21) #greater than
print(age >= 21) #greater than or equal to

# Each mathematical comparison can be used as part of an 'if' statement, which can help you detect the exact conditions of interest.