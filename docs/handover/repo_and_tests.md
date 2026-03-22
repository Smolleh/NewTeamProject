# Repository Structure
NewTeamProject/
|-docs/
|-- architecture/
|--- ReadMe.md
|-- data/
|--- ReadMe.md
|-- decisions/
|--- license-decisions.md
|-- handover/
|--- ReadMe.md
|--- data_management.md
|--- deployment.md
|--- development.md
|--- operations_and_maintenance.md
|--- repo_and_tests.md
|- museumProject/ 

# How to Run Tests
## First, in order to run the app:
1. in the terminal, naviagate to the NEWTEAMPROJECT repository (the one that pipfile is in)
2. run:
pipenv install (to install all dependencies)
3. run:
pipenv shell (to enter the virtual environment)
4. run:
cd museumProject
5. run:
python manage.py runserver

## Museum Testing:
1. Do the above (steps 1-4) 
2. run:
python manage.py test museumApp

## Quiz Testing:
1. Do the above (steps 1-4) 
2. run:
python manage.py test quizApp

if you have made any changes to the models.py file:
1. run: 
python manage.py makemigrations
2. run:
python manage.py migrate
3. run:
python manage.py runserver

