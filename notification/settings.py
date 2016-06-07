import dj_database_url

try:
    from .local_settings import *
except ImportError:
    pass

DEBUG = False
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']

DATABASES['default'] = dj_database_url.config()

