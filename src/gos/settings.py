"""
Django settings for gos project.

Generated by 'django-admin startproject' using Django 4.2.10.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path
import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: don't run with debug turned on in production!
# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, "gos", ".env"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY")


# False if not in os.environ because of casting above
DEBUG = env("DEBUG", False)

ALLOWED_HOSTS = ["*"] if DEBUG else ["www.gameofskateapp.com"]

# Application definition

# Default Django apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",  # needed for 'allauth.socialaccount'
]
# 3rd party apps
INSTALLED_APPS += [
    "rest_framework",
    # <social auth>
    "allauth",
    "allauth.account",
    "allauth.headless",
    # I don't know yet if i want mfa and usersessions
    # 'allauth.mfa',
    # 'allauth.usersessions',
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    # TODO: add apple after google works
    #'allauth.socialaccount.providers.apple',
    # https://docs.allauth.org/en/latest/socialaccount/providers/apple.html
    # </social auth>
]
# original apps
INSTALLED_APPS += []

SITE_ID = 1  # needed for 'allauth.socialaccount'

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # Add the account middleware: (allauth)
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "gos.urls"

TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, "templates"),
]
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": TEMPLATE_DIRS,
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "gos.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    # "default": {
    #     "ENGINE": "django.db.backends.postgresql",
    #     "NAME": env("DB_NAME"),
    #     "USER": env("DB_USER"),
    #     "PASSWORD": env("DB_PASSWORD"),
    #     "HOST": env("DB_HOST"),
    #     "PORT": env("DB_PORT"),
    # }
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }

}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
}
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by email
    "allauth.account.auth_backends.AuthenticationBackend",
)

ACCOUNT_EMAIL_REQUIRED = True
SOCIALACCOUNT_EMAIL_AUTHENTICATION_AUTO_CONNECT = (
    True  # if they have account w/ applle and google, same email, connect them.
)
SOCIALACCOUNT_ONLY = True  # this means cannot create local-only user account, only social (google, apple, etc)
HEADLESS_ONLY = True  # This means no browser login views

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
# # Reminder: edit the files in STATICFILES_DIRS. the ones in static are auto generated.
STATICFILES_DIRS = [os.path.join(BASE_DIR, "staticfiles")]
STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
STATIC_URL = "/static/"
MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# see https://docs.allauth.org/en/latest/socialaccount/configuration.html
SOCIALACCOUNT_EMAIL_AUTHENTICATION = True
SOCIALACCOUNT_ONLY = True
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_ADAPTER = 'auth.adapter.AccountAdapter'
SOCIALACCOUNT_ADAPTER = 'auth.adapter.SocialAccountAdapter'
# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    # For each OAuth based provider, either add a ``SocialApp``
    # (``socialaccount`` app) containing the required client
    # credentials, or list them here:
    "google": {
        "APPS": [
            {
                "client_id": env.str(
                    "DJANGO_SOCIALACCOUNT_GOOGLE_WEB_CLIENT_ID", default=""
                ),
                "secret": env.str("DJANGO_SOCIALACCOUNT_GOOGLE_WEB_SECRET", default=""),
                # key is not needed for google
            },                      
        ],
        # The following provider-specific settings will be used for all apps:
        "SCOPE": ["profile", "email",],
        "AUTH_PARAMS": {"access_type": "online",},
        "OAUTH_PKCE_ENABLED": True,
        "FETCH_USERINFO": False,
    },
}
