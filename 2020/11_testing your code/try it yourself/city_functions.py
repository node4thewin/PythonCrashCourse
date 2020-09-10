# Write a function that accepts two parameters: a city name and a country name. The function should return a single string of the form 'City, Country', such as 'Santiago, Chile'. Store the function in a module called 'city_functions.py'

def location(city, country):
  """Log a location with city and country."""
  display_city_country = f"{city}, {country}"
  return display_city_country.title()