"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
from dotenv import load_dotenv
import os

from .config_parse import yandex_mail
from .utils import find_env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_DIR = Path(__file__).resolve() / '.env'

load_dotenv(ENV_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
CACHE_ENABLE = True
GLOBAL_CACHE = True

ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS'),]
INTERNAL_IPS = ['127.0.0.1',]
SITE_ID = 1


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.redirects',
    'django.contrib.sites',
    
    #django_toolbar
    'debug_toolbar',
    
    #django_extensions
    'django_extensions',
    
    #crispy_forms
    'crispy_forms',
    'crispy_bootstrap5',
    
    #phonenumber_field
    'phonenumber_field',
    #countries
    'django_countries',
    
    #apps
    'home.apps.HomeConfig',
    'catalog.apps.CatalogConfig',
    'news.apps.NewsConfig',
    'users.apps.UsersConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    
    #django_debug_toolbar
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
if CACHE_ENABLE and GLOBAL_CACHE:
    MIDDLEWARE += [
        #global cache
        'django.middleware.cache.UpdateCacheMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.cache.FetchFromCacheMiddleware',
        ]
    
    
ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
                #context_processors custom
                'home.context_processors.get_base_model',
                'home.context_processors.get_product',
            ],
        },
    },
]

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
)

CRISPY_TEMPLATE_PACK = 'bootstrap5'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'elshop',
        'USER': 'postgres',
        'HOST': 'localhost',
        'PORT': 5433,
        'PASSWORD': os.environ.get('PASSWORD_POSTGRES'),
    }
}

if CACHE_ENABLE:
    match find_env('TEST'):
        case 'False':
            backend_cache = {
            'BACKEND': 'django.core.cache.backends.redis.RedisCache',
            'LOCATION': find_env('LOCATION_CACHE'),
            'TIMEOUT': 60 * 10,
            }
        case _:
            backend_cache = {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
            
    CACHES = {
    'default': backend_cache,
    }
    CACHE_MIDDLEWARE_KEY_PREFIX='el_shop_cache'
    CACHE_MIDDLEWARE_SECONDS=600

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Asia/Omsk'

USE_I18N = True

USE_TZ = True

PHONENUMBER_DEFAULT_REGION = 'RU'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [ BASE_DIR / 'static/' ]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'users.authentication.EmailAuthBackend',
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

YANDEX_MAIL = yandex_mail()
EMAIL_HOST = YANDEX_MAIL.get('host')
EMAIL_PORT = YANDEX_MAIL.get('port')
EMAIL_HOST_USER = YANDEX_MAIL.get('hostuser')
EMAIL_HOST_PASSWORD = os.environ.get('PASSWORD_HOST_YANDEX')
EMAIL_USE_SSL = True if YANDEX_MAIL.get('connecttype') == 'SSL' else False
EMAIL_USE_TLS = True if YANDEX_MAIL.get('connecttype') == 'TLS' else False

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER
EMAIL_ADMIN = EMAIL_HOST_USER

LOGIN_URL = 'users:login'
LOGOUT_REDIRECT_URL = 'home:home_page'
