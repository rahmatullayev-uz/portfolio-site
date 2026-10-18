"""
Local development settings.
"""

from .base import *  # noqa: F403

DEBUG = True
ALLOWED_HOSTS = ["*"]

# Lokal ishlab chiqishda WhiteNoise statik fayl keshini soddalashtirish
STORAGES["staticfiles"]["BACKEND"] = "django.contrib.staticfiles.storage.StaticFilesStorage"  # noqa: F405
