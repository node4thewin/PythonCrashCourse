# 9-11 Imported Admin

# Start with your work from Exercise 9-8 (page 173). Store the classes 'User', 'Privileges', and 'Admin' in one module. Create a separate file, make and 'Admin' instance, and call 'show_privileges()' to show that everything is working correctly.

from admin_module import User, Admin, Privileges

user1 = Admin('andrew', 'harvey', 'evrythngevl', 32)
user1.privileges.show_privileges()
