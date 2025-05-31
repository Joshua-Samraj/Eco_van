from .settings import *  # Import base settings

import os
from pathlib import Path

# Disable debug mode
DEBUG = False

# Allow only your production domain(s)
ALLOWED_HOSTS = ["https://eco-van.onrender.com/"]

# Secret key from environment variable
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "fallback-secret-if-not-set")

# Static & Media files
BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Add WhiteNoise to serve static files in production
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

# Database from environment (for PostgreSQL on Render, for example)
import dj_database_url

DATABASES = {
    "default": dj_database_url.config(
        default=os.getenv("DATABASE_URL")
    )
}

# Logging (optional, but helpful)
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": os.path.join(BASE_DIR, "logs/django.log"),
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}

# Default auto field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
