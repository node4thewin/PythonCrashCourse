# 8-2 FAVORITE BOOK

# Write a function called 'favorite_book()' that accepts one parameter, 'title'. The function should print a message, such as 'One of my favorite books is Alice in Wonderland'. Call the function , making sure to include a book title as an argument in the function call. 

def favorite_book(title):
  """Display message of Favorite Book"""
  msg = f"My favorite book is {title}."
  print(msg)
  
favorite_book('Alice in Wonderland') # this is an argument inside the function