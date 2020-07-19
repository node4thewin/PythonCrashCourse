# USING 'OR' TO CHECK MULTIPLE CONDITIONS

# The keyword 'or' allows you to check multiple conditions as well, but it passes when either or both of the individual tests pass. An 'or' expression fails only when both individual tests fail.

# Let's consider two ages again, but this time we'll look for only one person to be over 21:

age_0 = 22
age_1 = 18

print(age_0 >= 21 or age_1 >+ 21)
# showing the same statement but using ()
print((age_0 >= 21) or (age_1 >= 21))

age_0 = 18
print(age_0 >= 21 or age_1 >+ 21)
# showing the same statement but using ()
print((age_0 >= 21) or (age_1 >= 21))

# We start with two age variables again at line 7. Because the test for age_0 at line 10 passes, the overall expression evaluates to "true". We then lower age_0 to 18. In the test at line 15, both tests now fail and the overall expression evaluates to "false".