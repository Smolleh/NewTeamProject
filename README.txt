In order to access the repository clone using:
git clone https://github.com/Smolleh/NewTeamProject.git

*first time you run the app*
install pipenv (pip install pipenv, or however else you want to instal it)
ensure you cloned the github repository to your computer
ensure you are using the python 3.13 interpreter

in order to run the app:
1. in the terminal, naviagate to the NEWTEAMPROJECT repository (the one that pipfile is in)
2. run:
pipenv install (to install all dependencies)
3. run:
pipenv shell (to enter the virtual environment)
4. run:
cd museumProject
5. run:
python manage.py runserver

Testing:
1. Do the above (steps 1-4) 
2. run:
python manage.py test museumApp

if you have made any changes to the models.py file:
1. run: 
python manage.py makemigrations
2. run:
python manage.py migrate
3. run:
python manage.py runserver

Copyright <2026> <[Dominic Clegg], [Leo Hudson], [Sam James], [Alex Parsons], [Coco Bemand], [Jimi Manderville], [Dylan Ryan]>
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
