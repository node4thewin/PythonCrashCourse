# 8-16 Imports

# Using a program you wrote that has one function in it, store the function in a separate file. Import the function into your main program file, and call the function using each of these approaches:

# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *

import fav_book
fav_book.favorite_book('Harry Potter')

from fav_book import favorite_book
favorite_book('Harry Potter')

from fav_book import favorite_book as fb
fb('Harry Potter')

import fav_book as f_b
f_b.favorite_book('Harry Potter')

from fav_book import *
favorite_book('Harry Potter')