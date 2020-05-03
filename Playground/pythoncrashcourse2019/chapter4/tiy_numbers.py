# CHAPTER 4 TRY IT YOURSELF

# 4-3 Counting to Twenty
# Use a 'for' loop to print the number from 1 to 20, inclusively.

for value in range(1, 21):
	print(value)

for value in range(21):
	print(value)

# 4-4 One Million
# Make a list of numbers from one to one million. Then use a 'for'
# loop to print the numbers.

onemillion = list(range(1, 1000001))

for amillion in onemillion:
	print(amillion)

# 4-5 Summing One Million
# Make a list of the numbers from one to one million, and then use
# min() and max() to make sure the list starts and ends with one/one
# million. Also use the sum() function.

onemillion = list(range(1, 100001))
print(min(onemillion))
print(max(onemillion))
print(sum(onemillion))

