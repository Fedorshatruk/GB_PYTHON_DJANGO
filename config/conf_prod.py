import os

from .settings import *

DEBUG = False

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

DATABASES = {
    "default": {
    "ENGINE": "django.db.backends.postgresql_psycopg2",
    "NAME": "braniac",
    "USER": "django",
    "PASSWORD": "geekbrains",
    "HOST": "127.0.0.1",
    "PORT": "5432",
    }
}

del STATICFILES_DIRS
STATIC_ROOT = BASE_DIR / "static"