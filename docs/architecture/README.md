# Architecture Overview
The AI Failures Museum is a web-based application which was constructed using the Django framework. It's client-server style architecture allows users to interact with the frontend interface and requests are processed by the Django backend, connected to a SQLite database. The system is designed for the following functionality: exhibit browsing, quiz testing and curator management of the system. 


## System Components
### Frontend (HTML & CSS)
The frontend of the system is made up of HTML and CSS templates which allow the users of the system to browse the exhibits, read the details of each exhibit and complete quizzes to test their knowledge.
## Backend (Django)
The backend of the system utilizes the Django rest framework to process requests from the users and handle any communication between the frontend actions and the database. 
### Database (SQLite)
An SQLite database is used to store all the relevant information for each exhibit and their respective quizzes as well as user accounts.
### API
API endpoints are used to retrieve and manipulate the data in the sytem through the use of Django rest framework API views. 
### Authentication and Authorization
The authentication is achieved using the User model from the django auth library. This model implements sessions stored using cookies, which are used to authenticate the user preforming requests. The Authorization system enforces role-based access control to the system and establishes what a visitor can do compared to a curator. 

## Deployment View
Our system is deployed through the use of PythonAnywhere and at the domain name: bigleh.eu.pythonanywhere.com. This allows the users to access the system through a web browser. The server on PythonAnywhere clones the repository on GitHub which allows for easy updates to the system by pulling the latest version from the active development branch. 
