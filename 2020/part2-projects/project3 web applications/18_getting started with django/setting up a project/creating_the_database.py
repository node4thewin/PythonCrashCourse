# Creating the Database

# Django stores most of the information for a project in a database, so next we need to create a database that Django can work with. Enter the following command (still in an active environment):

# (ll_env)learning_log$ python manage.py migrate

# Anytime we modify a database, we say we're 'migrating' the database. Issuing the 'migrate' command for the first time tells Django to make sure the database matches the current state of the project. The first time we run this command in a new project using SQLite (more about SQLite in a moment), Django will create a new database for us. The 'Operations' line, reports that it will prepare the database to store information it needs to handle administrative and authentication tasks.

# Running the ls command shows that Django created another file called 'db.sqlite3'. SQLite is a database that runs off a single file; it's ideal for writing simple apps because you won't have to pay much attention to managing the database.

# NOTE - In an active environment, use the command 'python' to run manage.py commands, even if you use something different, like 'python3', to run other programs. In a virtual environment, the command python refers to the version of python that created the virtual environment.