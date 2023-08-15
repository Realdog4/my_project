from config.settings.base import *  # NOQA

DEBUG = True

ALLOWED_HOSTS = []

SECRET_KEY = "django-secret-key"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3", # NOQA
    }
}


STATIC_URL = "static/"
