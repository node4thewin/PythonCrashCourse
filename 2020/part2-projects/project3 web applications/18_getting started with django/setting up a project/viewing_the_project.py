# Viewing the Project

# Let's make sure that Django has set up the project properly. Enter the 'runserver' command as follows to view the project in its current state:

# ***
# (ll_env)learning_log$ python manage.py runserver
# Watchman unavailable: pywatchman not installed.
# Watching for file changes with StatReloader
# Performing system checks...

# System check identified no issues (0 silenced). 
# February 18, 2019 - 16:26:07
# Django version 2.2.0, using settings 'learning_log.settings'
# Starting development server at http://127.0.0.1:8000/
# Quit the server with CONTROL-C.
# ***

# Django should start a server called 'development server', so you can view the project on your system to see how well it works. When you request a page by entering a URL in a browser, the Django server responds to that request by building the appropriate page and sending it to the browser.

# At line 11, Django checks to make sure the project is set up properly; at line 13 it reports the version of Django in use and the name of the settings file in use; and at line 14 it reports the URL where the project is being served. The URL 'http://127.0.0.1:8000/ indicates that the project is listening for requests on port 8000 on your computer, which is called a localhost. The term 'localhost' refers to a server that only processes requests on your system; it doesn't allow anyone else to see the pages you're developing.

# Open a web browser and enter the URL 'http://localhost:8000/ or http://127.0.0.1:8000/ if the first one doesn't work. You should see something like Figure 18-1, a page that Django creates to let you know all is working properly so far. Keep the server running for now, but when you want to stop the server, press CTRL-C in the terminal where the 'runserver' command was issued. 

# NOTE - If you receive the error message 'That port is already in use', tell Django to use a different port by entering 'python manage.py runserver 8001', and then cycle through higher numbers until you find an open port.