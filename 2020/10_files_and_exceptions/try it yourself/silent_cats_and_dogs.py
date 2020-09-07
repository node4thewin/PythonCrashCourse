# 10-9 Silent Cats and Dogs

# Modify your 'except' block in Exercise 10-8 to fail silently if either file is missing.

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
  try:
    with open(filename) as f:
      contents = f.read()

  except FileNotFoundError:
    pass

  else:
    print(f"  {filename}:\n")
    print(contents)
  