import dj_database_url
import os

from .common import *

DEBUG = False

SECRET_KEY = os.environ["SECRET_KEY"]

ALLOWED_HOSTS = []

DATABASES = {"default": dj_database_url.config()}
