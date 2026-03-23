**to reset the database**
1. ensure you are in the virtual environment
2. navigate to NEWTEAMPROJECT/museumProject
3. enter the shell via python manage.py shell
4. in the sell, run:
    rm db.sqlite3
5. exit the shell via:
    exit()
6. run python manage.py makemigrations
7. run python manage.py migrate

**to create a developer user profile**
1. ensure you are in the virtual environment
2. navigate to NEWTEAMPROJECT/museumProject
3. run python manage.py createsuperuser
4. enter a username, email and password

**to assign a user as a moderator**
1. navigate to the admin pannel via:
2. sign in using your developer credentials
3. navigate to the users section
4. find the user you want to assign, and click edit
5. navigate to the groups section
6. assign the Developer group, and deassign the Visitor group 
7. click save



