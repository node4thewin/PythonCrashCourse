# 10-6 Addition

# One common problem when prompting for numerical input occurs when people provide text instead of numbers. When you try to convert the input to an 'int', you'll get a "ValueError". Write a program that prompts for two numbers. Add them together and print the result. Catch the 'ValueError' if either input value is not a number, and print a friendly error message. Test your program by entering two numbers and then by entering some text instead of a number.

print("Enter 'quit' at anytime to end the program.")
print("Type any two numbers and we'll add them together...")

try:
  first_number = input("\nFirst Number: ")
  second_number = input("Second Number: ")
  total = int(first_number) + int(second_number)
  print(f"The sum of those numbers is {total}.")

except ValueError:
  print("Please try again, make sure you enter a numbers (not letters).")