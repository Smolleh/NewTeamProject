in order to run the app:
make sure you have pipenv installed (pip install pipenv)
1. run pipenv install (to install all dependencies)
2. run pipenv shell (to enter the virtual environmenrt)
3. cd into museumProject
4. run python manage.py runserver

if you have made any changes to the models.py file:
1. run python manage.py makemigrations
2. run python manage.py migrate
3. run python manage.py runserver