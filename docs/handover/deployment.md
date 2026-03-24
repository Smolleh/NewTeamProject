# Required Services
- Python 3.13
- GitHub repo access
- PythonAnywhere
- pip / virtualenv

# Environment Variables
Based on Django configuration settings, the following environment settings should be configured within the PythonAnywhere WSGI file:
    - DJANGO_SECRET_KEY - A securely generated secret key for django. Seperate key used for development and production. 
    - DJANGO_SETTINGS_MODULE - should be set to museumProject.settings

Generating a secret key: 
    In the PythonAnywhere console input: python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# Step-By-Step Deployment Instructions

1. Clone the repository within the PythonAnywhere bash console with:
    git clone https://github.com/Smolleh/NewTeamProject.git

2. Construct and access a virtual environment with:
    cd NewTeamProject
    mkvirtualenv myenv --python=python3.13
    workon myenv

3. Checkout the correct and most up to date branch:
    git fetch origin
    git checkout <branch-name>
    git pull origin <branch-name>

4. Install required dependencies with: 
    pip install -r requirements.txt

5. Configure the WSGI file within the PythonAnywhere web tab, subsituting the secret key with the generated one:
    import sys
    import os

    os.environ['DJANGO_SECRET_KEY'] = 'your-generated-secret-key-here'

    path = '/home/bigleh/NewTeamProject/museumProject'
    if path not in sys.path:
    sys.path.append(path)

    os.environ['DJANGO_SETTINGS_MODULE'] = 'museumProject.settings'

    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()

6. Configure static and media files within the web tab: 
    URL - /static/ Directory - /home/bigleh/NewTeamProject/museumProject/staticfiles
    URL - /media/ Directory - /home/bigleh/NewTeamProject/museumProject/media

7. Run migrations within the PythonAnywhere bash console:
    cd ~/NewTeamProject/museumProject (if not within museumProject directory already)
    python manage.py migrate

8. Collect static files within the PythonAnywhere bash console:
    python manage.py collectstatic --noinput

9. Reload the web app within the web tab on PythonAnywhere and the website should now be deployed

# Updating to new versions #
Run these commands within the PythonAnywhere bash console:
    workon myenv
    cd ~/NewTeamProject
    git pull origin <branch-name>
    cd museumProject
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py collectstatic --noinput
