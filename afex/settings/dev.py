from decouple import config

from .common import *

DEBUG = True
SECRET_KEY = config("SECRET_KEY")

SITE_ID = 1

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "afex",
        "HOST": "localhost",
        "USER": "postgres",
        "PASSWORD": "1241-Biola",
    }
}
