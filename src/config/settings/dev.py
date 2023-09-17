import os

from config.settings.base import *  # NOQA

DEBUG = True

ALLOWED_HOSTS = []

SECRET_KEY = "django-secret-key"

DATABASES = {
    # "default": {
    #     "ENGINE": "django.db.backends.postgresql",
    #     "NAME": os.environ.get("POSTGRES_DB"),
    #     "USER": os.environ.get("POSTGRES_USER"),
    #     "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
    #     "HOST": os.environ.get("POSTGRES_HOST"),
    #     "PORT": os.environ.get("POSTGRES_PORT")
    # },
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # NOQA
    }
}


STATIC_URL = "static/"
