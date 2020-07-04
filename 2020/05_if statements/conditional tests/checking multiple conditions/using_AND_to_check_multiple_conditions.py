# Using 'and' to Check Multiple Conditions

# To check whether two conditions are both 'True' simultaneously, use the keywork 'and' to combine the two conditional tests; if each test passes, the overall expression evaluates to be 'True'. If either test fails or if both tests fail, the expression evaluates as 'False'.

# For example, you can check whether two people are both over 21 using the following test:

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

age_1 = 22
print(age_0 >= 21 and age_1 >= 21)

# At line 7 and 8 we define two ages (age_0 and age_1). At line 9 we check whether both ages are 21 or older. The test on the left passes, but the test on the right fails, so the overall conditional expression evaluates to 'False'. At line 11 we change 'age_1' to 22. The value of age_1 is now greater than 21, so both individual tests pass, causing the overall conditional expression to evaluate as 'True'.

# To improve readability, you can use parentheses around the individual tests, but they are not required. If you use parentheses, your test would look like this:

print((age_0 >= 21) and (age_1 >= 21))