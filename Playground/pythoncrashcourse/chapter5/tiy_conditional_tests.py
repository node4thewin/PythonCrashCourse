# 5-1 Conditional Tests: Write a series of conditional tests. Print
# a statement describing each test and your prediction for the
# results of each test and your prediction for the results of each
# test. Your code should look something like this:

car = 'subaru'
print(car)


print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("\nIt's easy to figure out that car does not equal 'mercedes'.")
print(car != 'mercedes')

favorite_foods = 'ice cream', 'pizza', 'burritos', 'cheeseburgers'

print("\nI am guessing one of your favorite foods are Hot Dogs.")
print(favorite_foods == 'Hot Dogs')

# 5-2 More Conditional Tests: You don't have to limit the number of
# tests you create to ten. If you want to try more comparisons,
# write more tests here. Have at least one True and one False result
# for each of the following:

# 1. Tests for equality and inequality with strings

drinking_age = 21
print(f"\nThe drinking age is {drinking_age}")
print(drinking_age == 21)

print(f"\nSo Dad that means I can have a beer right?")
print(drinking_age != 21)

# 2. Tests using the lower() method.
print("\nThis is an example of the lower() method.")
IPA = 'Stone'
print(IPA.lower() == 'stone')

# 3. Numerical tests involving equality and inequality, greater
# than or equal to, and less than or equal to.

print("\nThe following are the results of numerical tests related to the drinking age.\n")
drinking_age = 21
age_0 = 21
age_1 = 18

print(21 == drinking_age)
print(18 == drinking_age)
print(18 != drinking_age)
print(21 != drinking_age)
print(22 > drinking_age)
print(18 > drinking_age)
print(17 < drinking_age)
print(22 < drinking_age)
print(22 >= drinking_age)
print(18 >= drinking_age)
print(17 <= drinking_age)
print(22 <= drinking_age)

# 4. Tests using the "and" keyword and the "or" keyword.

print('\nThe following are tests using "and" and the "or" keywords.\n')

if age_1 != drinking_age and age_1 < 21:
    print("Sorry Charlie, you are too young to be drinking!")

if age_0 == drinking_age or age_0 >= 21:
    print("\nCongratulations, you're old enough to get hammered.\n")

# 5. Test whether an itime "is" and then whether it "is not" in a
# list.

beer = [
    'stone', 'bold rock', 'budweiser', 'lagunitas', 'belching beaver', 'port city'
    ]
print(beer)


print("\nI wonder what types of beers this bar has...")

print("\nLet's see if Bold Rock is on the list.")

if 'bold rock' in beer:
    print(f"Cool, I'll take a {beer[1].title()}")

print("\nI don't think they have Miller Lite.")

if 'miller lite' not in beer:
    print("Makes sense it's a shit beer anyway.")


