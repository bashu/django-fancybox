"""
Django settings for the example project.

https://docs.djangoproject.com/en/stable/topics/settings/
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "YOUR_SECRET_KEY"  # noqa: S105

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

PROJECT_APPS = [
    "fancybox",
]

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    *PROJECT_APPS,
]

ROOT_URLCONF = "example.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.i18n",
                "django.template.context_processors.request",
            ],
        },
    },
]

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}

# Static files (CSS, JavaScript, Images)

STATIC_URL = "static/"
