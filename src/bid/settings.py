"""
Django settings for bid project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
import re

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ss117_@#+#4ddxcv/c.\r#&DFHE-)h9afy%2923dfsfXCVe@!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*',]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #3rd
    'rest_framework',
    'djangular',

    #project
    'code_cats',
    'frontend',
    'products',
    'example',
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

ROOT_URLCONF = 'bid.urls'

WSGI_APPLICATION = 'bid.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

#TODO: https://docs.djangoproject.com/en/dev/topics/db/multi-db/
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'TEST_NAME': 'my_test_sql',
        'TEST_USER': 'test_sql_user',
        'TEST_PASSWORD': 'password'
    },
    # 'default_mongo': {
    #     'ENGINE': 'django_mongodb_engine',
    #     'NAME': 'bid',
    #     'USER': '',
    #     'PASSWORD': '',
    #     'HOST': 'localhost',
    #     'PORT': '27017',
    #     'SUPPORTS_TRANSACTIONS': False,
    #     'TEST_NAME': 'my_test_mongodb',
    #     'TEST_USER': 'test_mongo_user',
    #     'TEST_PASSWORD': 'password'
    # },
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

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
            'filename': 'mysite.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers':['file'],
            'propagate': True,
            'level':'DEBUG',
        },
        'MYAPP': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    }
}


# Travis-ci
if 'TRAVIS' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'kitty',
            'USER': 'postgres',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '',
        }
    }

# For Heroku - put heroku var manually on the server:
if 'HEROKU' in os.environ:
    try:
        import dj_database_url
        DATABASES['default'] = dj_database_url.config(default='postgres://localhost')
    except ImportError:
        pass


MEDIA_ROOT = ''
STATIC_ROOT = os.path.join(BASE_DIR, STATIC_URL.strip("/"))

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'layout'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'site_media')

