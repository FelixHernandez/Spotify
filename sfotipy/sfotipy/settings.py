"""
Django settings for sfotipy project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!hj&ickz$xe)w4sjwvb-vpprxg--87gdm+7^-lc%o0zxhjvl%2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True



ALLOWED_HOSTS = ['localhost']




# Application definition
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
        'django.core.context_processors.request',
        'sfotipy.context_processors.basico',
        )
GRAPPELLI_ADMIN_TITLE='Proyecto Sfotipy'

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'tablib',
    'userprofiles',
    'tracks',    
    'albums',
    'artists',
    'genders',
    'mockups',
    'django_extensions',
    'rest_framework',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'sfotipy.middlewares.PaisMiddleware',
)

ROOT_URLCONF = 'sfotipy.urls'

WSGI_APPLICATION = 'sfotipy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
DEFAULT_CHARSET = 'utf-8' 
FILE_CHARSET = 'utf-8'


LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_FINDER=(
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )

CACHES={
    'default':{
        'BACKEND':'redis_cache.RedisCache',
        'LOCATION': 'localhost:6379',
        'OPTIONS':{
            'DB':1,
            'PARSER_CLASS':'redis.connection.HiredisParser'
        }
    }
}

STATICFILES_STORAGE ='django.contrib.staticfiles.storage.CachedStaticFilesStorage'
MEDIA_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2]+['media'])
STATIC_ROOT= os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2]+['static'])
MEDIA_URL = '/media/'
#backends
# AUTHENTICATION_BACKENDS=(
#     'userprofiles.backends.EmailBackend',
#     )