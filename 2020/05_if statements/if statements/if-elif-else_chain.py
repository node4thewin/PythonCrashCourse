# THE if-elif-else CHAIN

# Often, you'll need to test more than two possible situations, and to evaluate these you can use Python's 'if-elif-else' syntax. Python executes only one block in an 'if-elif-else' chain. It runs each conditional test in order until one passes. When a test passes, the code following that test is executed and Python skips the rest of the tests.

# Many real-world situations involve more than two possible conditions. For example, consider an amusement park that charges different rates for different age groups:

#   Admission for anyone under age 4 is free.
#   Admission for anyone between the ages of 4 and 18 is $25.
#   Admission for anyone age 18 or older is $40.

# How can we use an 'if' statemtn to determine a person's admission rate? The following code tests for the age group of a person and then prints an admission price message:

age = 12

if age < 4:
  print("Your admission cost is $0.")
elif age < 18:
  print("Your admission cost is $25.")
# 18 or older your admission is 40
else:
  print("Your admission cost is $40.")

# Any age greater than 17 would cause the first two tests to fail. In these situations, the 'else' block would be executed and the admission price would be $40.

# Rather than printing the admission price within the 'if-elif-else' block, it would be more concise to set just the price inside the 'if-elif-else' chain and then have a simple print() call that runs after the chain has been evaluated:

age = 12

if age < 4:
  price = 0
elif age <18:
  price = 25
else:
  price = 40

print(f"\nYour admission cost is ${price}.")

# This code produces the same output as the previous example, but the purpose of the 'if-elif-else' chain is narrower. Instead of determining a price and displaying a message, it simply determines the admission price. In addition to being more efficient, this revised code is easier to modify than the originaly approach. To change the text of the output message, you would need to change only the one print() call rather than three separate print() calls.