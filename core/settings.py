<<<<<<< HEAD
import os
=======
import os 
>>>>>>> 863c3ae30dc322ab542405ec8a6832db8e77e4b4
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

<<<<<<< HEAD
SECRET_KEY = config("SECRET_KEY")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]
=======
SECRET_KEY =config('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
>>>>>>> 863c3ae30dc322ab542405ec8a6832db8e77e4b4


# Application definition

INSTALLED_APPS = [
<<<<<<< HEAD
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    # add to this specific location
    "daphne",
    "django.contrib.staticfiles",
    # my apps
    "chat",
    "accounts",
    # installed apps
    "channels",
    "django_bootstrap5",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
=======
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    #add to this specific location
    'daphne',
    'django.contrib.staticfiles',
    #my apps
    'chat',
    'accounts',
    #installed apps
    'channels',
    'django_bootstrap5',

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

ROOT_URLCONF = 'core.urls'

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
>>>>>>> 863c3ae30dc322ab542405ec8a6832db8e77e4b4
            ],
        },
    },
]

<<<<<<< HEAD
WSGI_APPLICATION = "core.wsgi.application"
=======
WSGI_APPLICATION = 'core.wsgi.application'
>>>>>>> 863c3ae30dc322ab542405ec8a6832db8e77e4b4


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
<<<<<<< HEAD
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
=======
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
>>>>>>> 863c3ae30dc322ab542405ec8a6832db8e77e4b4
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
<<<<<<< HEAD
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
=======
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
>>>>>>> 863c3ae30dc322ab542405ec8a6832db8e77e4b4
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

<<<<<<< HEAD
LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"
=======
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'
>>>>>>> 863c3ae30dc322ab542405ec8a6832db8e77e4b4

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

<<<<<<< HEAD
STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
=======
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
>>>>>>> 863c3ae30dc322ab542405ec8a6832db8e77e4b4

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

<<<<<<< HEAD
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ASGI_APPLICATION = "core.routing.application"

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# """
CHANNEL_LAYERS = {"default": {"BACKEND": "channels.layers.InMemoryChannelLayer"}}
=======
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ASGI_APPLICATION = "core.routing.application"

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

"""
CHANNEL_LAYERS = {
    "default":{
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}
>>>>>>> 863c3ae30dc322ab542405ec8a6832db8e77e4b4

"""
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer", 
        "CONFIG": {
            "hosts": [config("REDIS_CHANNEL_LAYER_URL")],
        },
    },
}
<<<<<<< HEAD
"""

LOGIN_REDIRECT_URL = "chat:index"
LOGOUT_REDIRECT_URL = "chat:index"
LOGIN_URL = "accounts:login"
=======
#"""

LOGIN_REDIRECT_URL= 'chat:index'
LOGOUT_REDIRECT_URL = 'chat:index'
LOGIN_URL = 'accounts:login'
>>>>>>> 863c3ae30dc322ab542405ec8a6832db8e77e4b4
