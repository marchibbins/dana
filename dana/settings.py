from os.path import abspath, join, dirname
import os

# Environment variables
def env_var(key, default=None):
    val = os.environ.get(key, default)
    if val == 'True':
        val = True
    elif val == 'False':
        val = False
    return val

# Site
SITE_ID = 1
SITE_ROOT = abspath(join(dirname(__file__), '..'))
ALLOWED_HOSTS = ['*']

# Static
STATIC_ROOT = join(SITE_ROOT, 'static')
STATIC_URL = '/static/'

# Media
MEDIA_ROOT = join(SITE_ROOT, 'media')
MEDIA_URL = '/media/'

# Project
PROJECT_ROOT = abspath(dirname(__file__))

# Debugging
DEBUG = env_var('DEBUG', False)
TEMPLATE_DEBUG = DEBUG

# Templates
TEMPLATE_DIRS = (
    join(PROJECT_ROOT, 'templates'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

ADMINS = (
    ('Marc Hibbins', 'marc@marchibbins.com'),
)

MANAGERS = ADMINS

ROOT_URLCONF = 'dana.urls'
WSGI_APPLICATION = 'dana.wsgi.application'
SECRET_KEY = '$q(7&amp;*n=bs=z!^g223$1wdua@bi#r(4lj3#98wcgy0*i4)j371'

TIME_ZONE = 'Europe/London'
LANGUAGE_CODE = 'en-gb'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Apps
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
)

# Middleware
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
