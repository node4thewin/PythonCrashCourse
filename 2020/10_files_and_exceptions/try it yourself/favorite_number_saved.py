import json

fav_num = input("Enter your favorite number: ")
filename = 'fav_num.json'

with open(filename, 'w') as f:
  json.dump(fav_num, f)
