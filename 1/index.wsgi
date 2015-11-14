import sys
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
sys.path.append(os.path.join(os.path.dirname(__file__), 'bookapp'))
import sae
from bookapp import wsgi
application = sae.create_wsgi_app(wsgi.application)