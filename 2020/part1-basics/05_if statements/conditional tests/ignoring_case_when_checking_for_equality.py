# IGNORING CASE WHEN CHECKING FOR EQUALITY

# Testing for equality is case sensitive in Python. For example, two values with different capitalization are not considered equal:

car = 'Audi'
print(car=='audi')

# If case matters, this behavior is advantageous. But if case doesn't matter instead you just want to test the value of a variable, you can convert the variable's value to lowercase before doing the comparison:

print(car.lower() == 'audi')

# This test would return 'True' no matter how the value 'Audi' is formatted because the test is now case insensitive. The lower() function doesn't change the value that was originally stored in 'car', so you can do this kind of comparison without affecting the original variable.

print(car)

# At line 5 we assign the capitalized string 'Audi' to the variable car. At line 10 we convert the value of 'car' to lowercase and compare the lowercase value to the string 'audi'. The two strings match, so Python returns 'True'. At line 14 we can see that the value stored in 'car' has not been affected by the lower() method.

# Websites enforce certain rules for the data that users enter in a manner similar to this. For example, a site might use a conditional test like this to ensure that every user has a truly unique username, not just a variation on the capitalization of another person's username. When someone submits a new username, that new username is converted to lowercase and compared to the lowercase versions of all existing usernames. During this check, a username like 'John' will be rejected if any variation of 'john' is already in use.
