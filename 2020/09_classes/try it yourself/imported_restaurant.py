# 9-10 Imported Restaurant

# Using your latest 'Restaurant' class, store it in a module. Make a separate file that imports Restaurant. Make a Restaurant instance, and call one of Restaurant's methods to show that the import statement is working properly.

from restaurant_module import Restaurant

tortilla_factory = Restaurant('tortilla factory', 'mexican')
tortilla_factory.describe_restaurant()

