# OMITTING THE 'else' BLOCK

# Python does not require an 'else' block at the end of an if-elif chain. Sometimes an 'else' block is useful; sometimes it is clearer to use an additional elif statement that catches the specific condition of interest:

age = 66

if age < 4:
  price = 0
elif age < 18:
  price = 25
elif age < 65:
  price = 40
# ending with elif here instead of else like 'using_multiple_elif_blocks.py'
elif age >= 65:
  price = 20

print(f"\nYour admission cost is {price}.")

# The extra 'elif' blcok at line 14 assigns a price of $20 when the person is 65 or older, which is a bit clearer than the general 'else' block. With this change, every block of code must pass a specific test in order to be executed.

# The 'else' block is a catchall statement. It matches any condition that wasn't matched by a specific 'if' or 'elif' test, and that can sometimes include invalid or even malicious data. If you have a specific final condition you are testing for, consider using a final 'elif' block and omit the 'else' block. As a result, you'll gain extra confidence that your code will run only under the correct conditions.