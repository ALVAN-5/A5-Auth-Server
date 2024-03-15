import os, sys
# add the hellodjango project path into the sys.path
sys.path.append('.')

# add the virtualenv site-packages path to the sys.path
sys.path.append('../venv/lib/python3.12/site-packages')

# poiting to the project settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "a5_auth_server.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
