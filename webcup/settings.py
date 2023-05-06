import io
import os
from urllib.parse import urlparse

import environ

# Import the original settings from each template
from .basesettings import *

# Load the settings from the environment variable
env = environ.Env()


# check if file exist
if os.path.exists('.env'):
    env.read_env('.env')
else:
    env.read_env(io.StringIO(os.environ.get("APPLICATION_SETTINGS", None)))

# Setting this value from django-environ

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['http://localhost:3000', 'http://*']

# Default false. True allows default landing pages to be visible
DEBUG = env("DEBUG", default=False)

HOST = env("HOST", default=None)



if "webcup" not in INSTALLED_APPS:
     INSTALLED_APPS += ["webcup"] # for custom data migration

STATIC_ROOT = 'static/'