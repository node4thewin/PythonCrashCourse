# 4-5 SUMMING A MILLION

# make a list of the numbers from one to a million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.

million = list(range(1000001))
print(min(million))
print(max(million))
print(sum(million))
