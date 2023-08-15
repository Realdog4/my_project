from config.settings.base import *  # NOQA

DEBUG = False

ALLOWED_HOSTS = []

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-8377*uguf5mtylmh#klo3b!0kv$87tdg_milhe)$g1jk77xzx*"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3", # NOQA
    }
}

STATIC_URL = "static/"
