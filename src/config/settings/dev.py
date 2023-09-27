import os

from config.settings.base import *  # NOQA

DEBUG = True

ALLOWED_HOSTS = []

SECRET_KEY = "django-secret-key"

if os.environ.get("GITHUB_WORKFLOW"):
    DATABASES = {
            # "default": {
            #     "ENGINE": "django.db.backends.postgresql",
            #     "NAME": "tsehychko",
            #     "USER": "btsehychko",
            #     "PASSWORD": "123",
            #     "HOST": "localhost",
            #     "PORT": 5432
            # },
            "default": {
                "ENGINE": "django.db.backends.postgresql",
                "NAME": "postgres",
                "USER": "postgres",
                "PASSWORD": "postgres",
                "HOST": "0.0.0.0",
                "PORT": 5432,
            }
        }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("POSTGRES_DB"),
            "USER": os.environ.get("POSTGRES_USER"),
            "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
            "HOST": os.environ.get("POSTGRES_HOST"),
            "PORT": os.environ.get("POSTGRES_PORT")
        },
        "sqllite": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",  # NOQA
        }
    }


STATIC_URL = "static/"
