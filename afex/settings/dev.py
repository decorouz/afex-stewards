from decouple import config

from .common import *

DEBUG = True

SECRET_KEY = config("SECRET_KEY")


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "afex",
        "HOST": "localhost",
        "USER": "postgres",
        "PASSWORD": "1241-Biola",
    }
}
