from os.path import abspath, join, dirname
from os import environ

# Environment variables
def env_var(key, default=None):
    val = environ.get(key, default)
    if val == 'True':
        val = True
    elif val == 'False':
        val = False
    return val

# Paths
SITE_ROOT = abspath(join(dirname(__file__), '..'))
PROJECT_ROOT = abspath(dirname(__file__))

# Site
SITE_ID = env_var('SITE_ID', 1)
ALLOWED_HOSTS = ['*']

# Static
STATIC_ROOT = join(SITE_ROOT, 'static')
STATIC_URL = '/static/'

# Media
MEDIA_ROOT = join(SITE_ROOT, 'media')
MEDIA_URL = '/media/'

# Debugging
DEBUG = env_var('DEBUG', False)
TEMPLATE_DEBUG = DEBUG

# Templates
TEMPLATE_DIRS = (
    join(PROJECT_ROOT, 'templates'),
)

DATABASES = {
    'default': {
        'ENGINE': env_var('DB_ENGINE', ''),
        'NAME': env_var('DB_NAME', ''),
        'USER': env_var('DB_USER', ''),
        'PASSWORD': env_var('DB_PASSWORD', ''),
        'HOST': env_var('DB_HOST', ''),
        'PORT': env_var('DB_PORT', ''),
    }
}

ADMINS = (
    ('Marc Hibbins', 'marc@marchibbins.com'),
)

MANAGERS = ADMINS

ROOT_URLCONF = 'dana.urls'
WSGI_APPLICATION = 'dana.wsgi.application'

SECRET_KEY = env_var('SECRET_KEY', '')

TIME_ZONE = env_var('TIME_ZONE', 'Europe/London')
LANGUAGE_CODE = env_var('LANGUAGE_CODE', 'en-gb')
USE_I18N = env_var('USE_I18N', False)
USE_L10N = env_var('USE_L10N', True)
USE_TZ = env_var('USE_TZ', True)

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
