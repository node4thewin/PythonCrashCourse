# "if" Statements
# This is an example of one of the simplest "if" statements.
# ex. 
# if "contitional_test:"
# do something

age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

# if-else Statements

age = 17
if age >= 18:
    print("\nYou are old enough to vote!")
    print("Have you registered to vote yet?")

else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!\n")

# The if-elif-else Chain

# Often you'll need to test more than two possible situations.
# In order to evaluate this you'll need to use if-elif-else syntax.
# It runs each conditional test in order until one passes. It
# essentially waits until one of the tests passes.

# Admissions Example
# Consider an amusement park that charges different rates for
# different age groups:

# 1. Admission for anyone under age 4 is free.
# 2. Admission for anyone between ages of 4 and 18 is $25.00.
# 3. Admission for anyone age 18 or older is $40.

age = 12

if age < 4:
    print("Your admission cost is $0.")

elif age < 18:
    print("Your admission cost is $25.")

else:
    print("Your admission cost is $40.")

age = 47

print(f"\nWhat if my age is {age}?\n")

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.")

