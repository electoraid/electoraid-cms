"""
Django settings for electoraid_cms project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import django_heroku 
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6bmk0%w%+1drv7_!u5)-go-i6%)+^z8+)4#q9q@9-_rynhs1!a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django_admin_generator',
    'baton',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'electoraid.apps.ElectoraidConfig',
    'ilcampaigncash',
    'reversion',
    'baton.autodiscover',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'electoraid_cms.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'electoraid_cms.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'electoraid_cms',
        'USER': 'electoraid',
        'PASSWORD': 'electoraid_reporter',
        'HOST': 'localhost',
        'POST': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'


# Baton theme
BATON = {
    'SITE_HEADER': 'CHI.VOTE',
    'SITE_TITLE': 'CHI.VOTE',
    'INDEX_TITLE': 'Site administration',
    'SUPPORT_HREF': 'https://github.com/electoraid/electoraid-cms/issues',
    'COPYRIGHT': 'copyright © 2019 The Chicago Reporter', # noqa
    'POWERED_BY': '<a href="https://electoraid.org">The Chicago Reporter Electoraid Project</a>',
    'CONFIRM_UNSAVED_CHANGES': True,
    'SHOW_MULTIPART_UPLOADING': True,
    'ENABLE_IMAGES_PREVIEW': True,
    'MENU': (
        {
            'type': 'model',
            'app': 'electoraid',
            'name': 'person',
            'label': 'People',
            'icon': 'fa fa-user-circle',
        },
        {
            'type': 'model',
            'app': 'electoraid',
            'name': 'election',
            'label': 'Elections',
            'icon': 'fa fa-check-square',
        },
        {
            'type': 'model',
            'app': 'electoraid',
            'name': 'politicalbody',
            'label': 'Political bodies',
            'icon': 'fa fa-university',
        },
        {
            'type': 'model',
            'app': 'electoraid',
            'name': 'office',
            'label': 'Political offices',
            'icon': 'fa fa-id-card',
        },
        {
            'type': 'model',
            'app': 'electoraid',
            'name': 'politicalactioncommittee',
            'label': 'Committees',
            'icon': 'fa fa-hand-holding-usd',
        },
        {
            'type': 'app',
            'name': 'auth',
            'label': 'Admin',
            'icon': 'fa fa-lock',
            'models': (
                {
                    'name': 'user',
                    'label': 'Users'
                },
                {
                    'name': 'group',
                    'label': 'Groups'
                },
            )
        },
    ),
    # 'ANALYTICS': {
        # 'CREDENTIALS':  'noop.json', # os.path.join(BASE_DIR, 'credentials.json'),
        # 'VIEW_ID': '12345678',
    # }
}

django_heroku.settings(locals())