import os
from django.utils.translation import ugettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ROOT_PATH = os.path.dirname(os.path.realpath(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '{{ pillar["settings"]["secret_key"] }}'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = {{pillar["settings"]["debug"]}}

TEMPLATE_DEBUG = {{pillar["settings"]["template_debug"]}}

ENV = '{{pillar["settings"]["environment"]}}'

ALLOWED_HOSTS = [{{pillar["settings"]["allowed_hosts"]}}]

# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'huey.djhuey',

    'apps.core.cli',
    'apps.web',
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
    'django.middleware.csrf.CsrfViewMiddleware',
)

# URLs configurations

ROOT_URLCONF = 'system.urls'

# Define wsgi application

WSGI_APPLICATION = 'system.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': '{{ pillar["postgresql"]["database"] }}',
        'USER': '{{ pillar["postgresql"]["user"] }}',
        'PASSWORD': '{{ pillar["postgresql"]["password"] }}',
        'PORT': '{{ pillar["postgresql"]["port"] }}',
        'HOST': '{{ pillar["postgresql"]["host"] }}',
    }
}

# Huey

HUEY = {
    'backend': 'huey.backends.redis_backend',
    'name': 'huey',
    'connection': {
        'host': 'localhost',
        'port': 6379
    },
    'always_eager': False,
    'consumer_options': {
        'workers': 4
    },
}

# Templates

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages'
)

TEMPLATE_DIRS = (
    os.path.join(ROOT_PATH, 'templates'),
)

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGES = (
    ('en', _('LANGUAGE_LABEL_ENGLISH')),
    ('ru', _('LANGUAGE_LABEL_RUSSIAN')),
)

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(ROOT_PATH, 'static', 'static_root')
STATICFILES_DIRS = (
    os.path.join(ROOT_PATH, 'static', 'static_dirs'),
)

MEDIA_ROOT = os.path.join(ROOT_PATH, 'static', 'media')
MEDIA_URL = '/media/'

# Django rest framework

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'PAGINATE_BY': 10,
    'PAGINATE_BY_PARAM': 'per_page',
    'MAX_PAGINATE_BY': 100,
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}

# Django Rest Swagger

SWAGGER_SETTINGS = {
    'is_authenticated': True,
    'is_superuser': True,
}