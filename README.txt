*first time you run the app*
install pipenv (pip install pipenv, or however else you want to instal it)
ensure you cloned the github repository to your computer
ensure you are using the python 3.13 interpreter

in order to run the app:
1. in the terminal, naviagate to the NEWTEAMPROJECT repository (the one that pipfile is in)
2. run pipenv install (to install all dependencies)
3. run pipenv shell (to enter the virtual environmenrt)
4. cd into museumProject
5. run python manage.py runserver

if you have made any changes to the models.py file:
1. run python manage.py makemigrations
2. run python manage.py migrate
3. run python manage.py runserver