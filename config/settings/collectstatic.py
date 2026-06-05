"""Minimal settings for running collectstatic at build time."""
from .base import *  # noqa
from .base import env

DATABASES = {}
CACHES = {"default": {"BACKEND": "django.core.cache.backends.dummy.DummyCache"}}
JWKS = {}
