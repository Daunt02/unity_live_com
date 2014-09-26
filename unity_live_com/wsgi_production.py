import os
import sys

import site
from os import urandom

site.addsitedir(
    '/home/nerdfiles/.virtualenvs/jahjah_works/lib/python2.7/site-packages')

from django.core.handlers.wsgi import WSGIHandler

os.environ['DJANGO_SETTINGS_MODULE'] = 'jahjah_works.settings'

activate_this = os.path.expanduser(
    "~/.virtualenvs/jahjah_works/bin/activate_this.py")
execfile(activate_this, dict(__file__=activate_this))

project = '/home/nerdfiles/webapps/jahjah_works/jahjah_works/'
sys.path.insert(0, project)
workspace = os.path.dirname(project)
sys.path.append(workspace)

application = WSGIHandler()
