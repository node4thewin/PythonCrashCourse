# Modify your function so it requires a third parameter, 'population'. It should now return a single string of the form 'City, Country - population ...' such as Santiago, Chile - population 5000000000. Run test_cities.py again. Make sure test_city_country() fails this time.

def location(city, country, population=0):
  """Log a location with city, country, and population."""

  display_function = f"{city.title()}, {country.title()}"
  
  if population:
    display_function += f" - population {population}"
  return display_function