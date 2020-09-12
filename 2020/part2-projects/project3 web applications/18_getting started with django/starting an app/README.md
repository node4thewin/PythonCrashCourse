# Starting an App

A Django 'project' is organized as a group of individual 'apps' that work together to make the project work as a whole. For now, we'll create just one app to do most of our project's work. We'll add another app in Chapter 19 to manage user accounts.

You should leave the developmentserver running in the terminal window you opened earlier. Open a new terminal window (or tab) and navigate to the directory that contains 'manage.py'. Activate the virtual environment, and then run the 'startapp' command:

learning_log$ source ll_env/bin/activate
(ll_env)learning_log$ python manage.py startapp learning_logs
(ll_env)learning_log$ ls
db.sqlite3 learning_log learning_logs ll_env manage.py
(ll_env)learning_log$ ls learning_logs/
__init__.py admin.py apps.py migrations models.py tests.py views.py

The command 'startapp' 'appname' tells Django to create the infrastructure needed to build an app. When you look in the project directory now, you'll see a new folder called 'learning_logs' (line 9). Open that folder to see what Django has created (line 11). The most important files are 'models.py', 'admin.py', and 'views.py'. We'll use 'models.py' to define the data we want to manage in our app. We'll look at 'admin.py' and 'views.py' a little later.