# USING int() TO ACCEPT NUMERICAL INPUT

# When you use the 'input()' function, Python interprets everything the user enters as a string. Consider the following interpreter session, which asks for the user's age:

# USE THE TERMINAL/PYTHON FOR THIS

# >>> age = input("How old are you? ")
# How old are you? 21
# >>> age
# '21'

# The user enters the number 21, but when we ask Python for the value of age it returns '21', the string representation of the numerical value entered. We know Python interpreted the input as a string because the number is enclosed in quotes '21' vs. just 21. If all you want to do is print the input, this works well. BUT if you try to use the input as a number, you'll get an error:

# >>> age = input("How old are you? ")
# How old are you? 21
# >>> age >= 18
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: '>=' not supported between instances of 'str' and 'int'

# When you try to use the input to do a numerical comparison (line 16), Python produces an error because it can't compare a string to an integer: the string '21' that's assigned to 'age' can't be compared to the numerical value 18 (line 19).

# We can resolve this issue by using the 'int()' function, which tells Python to treat the input as a numerical value. The 'int()' function converts a string representation of a number to a numerical representation, as shown below:

# >>> age = input("How old are you? ")
# How old are you? 21
# >>> age = int(age)
# >>> age >= 18
# True

# In this example, when we enter 21 at the prompt, Python interprets the number as a string, but the value is then converted to a numerical representation by int() at line 27. Now Python can run the conditional test: it compares age (which now represent the numerical value of 21 vs the string value of 21) and 18 to see if 'age' is greater than or equal to 18. This test evaluates to 'True'.

# SEE 'using_int_in_actual_program.py FOR MORE...