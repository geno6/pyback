"""
Django settings for project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os
from django.utils.translation import ugettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ROOT_PATH = os.path.dirname(os.path.realpath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '{{ pillar["settings"]["secret_key"] }}'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = {{ pillar["settings"]["debug"] }}

TEMPLATE_DEBUG = {{ pillar["settings"]["template_debug"] }}

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.home',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'system.urls'

WSGI_APPLICATION = 'system.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.postgresql_psycopg2",
        'NAME': "{{ pillar['postgresql']['database'] }}",
        'USER': "{{ pillar['postgresql']['user'] }}",
        'PASSWORD': "{{ pillar['postgresql']['password'] }}",
    }
}

# Templates

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.static',
)

TEMPLATE_DIRS = (
    os.path.join(ROOT_PATH, "../templates"),
)

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGES = (
    ("en", _("English")),
    ("ru", _("Russian")),
)

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


LOCALE_PATHS = (
    os.path.join(BASE_DIR, "locale"),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(ROOT_PATH, "../static")

# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(ROOT_PATH, "../logs/django.log"),
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'apps.api': {
            'propagate': True,
            'handlers': ['file'],
            'level': 'DEBUG',
        },
        'apps.home': {
            'propagate': True,
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    }
}