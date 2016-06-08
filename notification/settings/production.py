__author__ = 'stikks'
import dj_database_url

from .local import *

DEBUG = False
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']

DATABASES['default'] = dj_database_url.config()

