# 4-8 CUBES

# A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10).

cubes = []
for value in range(1,11):
  cube = value**3
  cubes.append(cube)

# Then use a 'for' loop to print out the value of each cube.

for cube in cubes:
  print(cube)


