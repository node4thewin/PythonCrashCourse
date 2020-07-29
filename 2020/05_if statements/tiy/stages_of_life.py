# 5-6 STAGES OF LIFE:

# Write an if-elif-else chain that determines a person's stage of life. Set a value for the variable 'age', and then:

# If the person is less than 2 years old, print a message that the person is a baby.
# If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
# If the person is 4 years old but less than 13, print a message that the person is a kid.
# If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
# If the person is at least 20 years old but less than 65, print a message saying that the person is an adult.
# If the person is age 65 or older, print a message that the person is an elder.

age = 66

if age < 2:
  print(f"You are a baby. Grow up.\n")

elif age >=2 and age <= 13:
  print(f"You're a kid. Humble yourself.\n")

elif age > 13 and age <= 20:
  print(f"You're a teenager acting like a child right now.\n")

elif age > 20 and age <= 65:
  print(f"You made it you're an adult. Throw away your teddy bear.\n")

else:
  print(f"You're old AF.\n")
