# Troubleshooting #

500 errors - Check error log on PythonAnywhere if deployed, if running locally see terminal output and browser error page.

Missing Modules - Run pipenv install <module-name> when running locally, or pip install <module-name> within the virtual environment on PythonAnywhere if deployed

Static/media files not loading - Verify static files are being correctly pointed to by PythonAnywhere. If they are collect static files with: python manage.py collectstatic --noinput , and hard refresh with:
Mac — Cmd + Shift + R
Windows/Linux — Ctrl + Shift + R or Ctrl + F5
If on mobile clear chache in browser settings, then refresh




