# 8-6 City Names

# Write a function called 'city_country()' that takes in the name of a city and its country. The function should return a string formatted like this:

# "Santiago, Chile"

# Call your function with at least three city-country pairs, and print the values that are returned.

def city_country(city, country):
  display_city_country = f"{city}, {country}"
  return display_city_country.title()

place = city_country('paris', 'france')
print(place)
place = city_country('Baltimore', 'USA')
print(place)
place = city_country('Banff', 'Canada')
print(place)

# Solution from Website

def city_country2(city, country):
  """Return a string like 'Santiago, Chile'."""
  return f"{city.title()}, {country.title()}"

city = city_country2('santiago', 'chile')
print(city)

city = city_country2('paris', 'france')
print(city)

city = city_country2('baltimore', 'maryland')
print(city)