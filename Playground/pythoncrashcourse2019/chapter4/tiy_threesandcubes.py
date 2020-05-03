# TRY IT YOURSELF
# 4-7 Threes

# Make a list of the multiples of 3 from 3 to 30. Use a for loop
# to print the numbers on your list.

threes = list(range(3, 31, 3))

for number in threes:
	print(number)

# 4-8 Cubes
# A number raised to the third power is called a cube. For example,
# the cube is 2 is written as 2**3 in Python. Make a list of the 
# first 10 cubes (that is, the cube of each integer from 1 
# through 10), and use a for loop to print out the value of each
# cube.

# Example 1 (more dense)
cubes = []
for value in range(1, 11):
	cube = value**3
	cubes.append(cube)

for cube in cubes:
	print(cube)

# Example 2 (less dense)

cubes = []
for value in range(1, 11):
	cubes.append(value**3)

print(cubes)

# Example 3 (least dense, and not for beginners)

# 4-9 Cube Comprehension
# Use a LIST COMPREHENSION to generate a list of the first 10 cubes.

cubes = [value**3 for value in range(1, 11)]
print(cubes)
