# Repository Structure
```
NewTeamProject/
├── docs/ #Stores all the documentation files
│   ├── architecture/ #Stores a ReadMe file which describes the main system components and provides a component diagram
│   │   
│   ├── data/ #Stores a ReadMe file which describes the data model and passport schema as well as the UML of the database
│   │   
│   ├── decisions/ #Stores a license decisions file which has the license we used
│   │  
│   └── handover/ #Contains several files to fully describe to a client how to install, operate, maintain and extend our system
│       
└── museumProject/
```

# How to Run Tests
## First, in order to run the tests:
1. in the terminal, naviagate to the NEWTEAMPROJECT repository (the one that pipfile is in)
2. run:
pipenv install (to install all dependencies)
3. run:
pipenv shell (to enter the virtual environment)
4. run:
cd museumProject

## Museum Testing:
1. Do the above (steps 1-4) 
2. run:
python manage.py test museumApp

## Quiz Testing:
1. Do the above (steps 1-4) 
2. run:
python manage.py test quizApp
