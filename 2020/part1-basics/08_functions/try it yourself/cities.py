# 8-5 CITIES

# Write a function called 'describe_city()' that accepts the name of a city and its country. The function should print a simple sentence, such as 'Reykjavik is in Iceland'. Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.

def describe_city(city, country='USA'):
  print(f"{city.title()} is in the {country}.")

describe_city('Washington, DC')
describe_city('herndon')
describe_city('Paris')