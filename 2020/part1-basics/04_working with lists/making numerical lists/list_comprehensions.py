# LIST COMPREHENSIONS

# The approach described earlier for generating the list "squares" consisted of using three or four lines of code. A "list comprehension" allows you to generate this same list in just one line of code. A list comprehension combines the "for" loop and the creation of new elements into one line, and automatically appends each new element. List comprehensions are not always presented to beginners, but I have included them here because you'll most likely see them as soon as you start looking at other people's code.

# The following example builds the same list of square numbers you saw earlier but uses a list comprehension:

squares = [value**2 for value in range(1, 11)]
print(squares)

# To use this syntax, begin with a descriptive name for the list, such as "squares". Next, open a set of square brackets and define the expression for the values you want to store in the new list. In this example the expression is value**2, which raises the value to the second power. Then, write a "for" loop to generate the numbers you want to feed into the expression, and close the square brackets. The "for" loop in this example is for "value in range(1, 11)", which feeds the values 1 through 10 into the expression value**2. Notice that no colon is used at the end of the "for" statement.

# It takes practice to write your own list comprehensions, but you'll find them worthwhile once you become comfortable creating ordinary lists. When you're writing three or four lines of code to generate lists and it begins to feel repetitive, consider writing your own list comprehensions.

