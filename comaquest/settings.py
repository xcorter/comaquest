"""
Django settings for comaquest project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_6wg8vaz1alc*^ii9u$ws0s932wi6bii97-!08orb4=4cq50l7'

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'main',
    'constance',
    'constance.backends.database',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'comaquest.urls'

WSGI_APPLICATION = 'comaquest.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
isDev = ""
configPath = os.path.join(os.path.dirname(__file__), ".config")
if os.path.exists(configPath):
    with open(configPath, "r") as config:
        isDev = config.read().replace('\n', '')
if isDev == "dev":
    db = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
    debug = True
else:
    db = {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'iquest',
        'USER': 'comaquestdb',
        'PASSWORD': 'gjhwp832zs',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
    debug = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = debug


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_CONTEXT_PROCESSORS += ('constance.context_processors.config',)

CONSTANCE_CONFIG = {
    "SLIDER_TIME" : (1000, "Время переключения слайдера"),
}

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
_PATH = os.path.abspath(os.path.dirname(__file__))

MEDIA_ROOT = os.path.join(_PATH, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(_PATH, 'static')
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_JQUERY_URL = STATIC_URL + "main/js/jquery.js"