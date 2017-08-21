import os
from .common import *

DEBUG = False
ALLOWED_HOSTS = ['*']

STATIC_ROOT = os.path.join(BASE_DIR, "..", "staticfiles") MEDIA_ROOT = os.path.join(BASE_DIR, "..", "media")
