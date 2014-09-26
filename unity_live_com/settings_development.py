# -*- coding: utf-8 -*- #

import os

try:
    from .settings_production import *
except ImportError:
    pass

ALLOWED_HOSTS = ['*']

DEBUG = True
LOCAL_DEVELOPMENT = True

# == DB ======================================= #

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.sqlite3',
        # Or path to database file if using sqlite3.
        'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite'),
        }
}
