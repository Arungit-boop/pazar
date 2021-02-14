"""
Django settings for PazarSite project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
from django.contrib.messages import constants as messages
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!jqj77r-qd0e$d8p@e#r)=lf&k(6vd2=5ic=&&)y0b)sgetxp3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'blog.apps.BlogConfig',
    'accounts.apps.AccountsConfig',
    'pazar.apps.PazarConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',
    # 'social_django',
    'taggit',
    'crispy_forms',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    # 'rollyourown.seo',
    'mapbox_location_field',
    'ckeditor',
    'ckeditor_uploader',
    'widget_tweaks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'PazarSite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'social_django.context_processors.backends', 
                # 'social_django.context_processors.login_redirect',
                # "django.core.context_processors.request",
            ],
        },
    },
]

WSGI_APPLICATION = 'PazarSite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'accounts.CustomUser'

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

#Added By Me
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

#Managing Media
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Messages built-in framework
MESSAGE_TAGS = {
    messages.DEBUG: 'secondary',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}

# Third party apps configuration
CRISPY_TEMPLATE_PACK = 'bootstrap4'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

AUTHENTICATION_BACKENDS = [
    'accounts.backends.EmailBackend',
    # 'django.contrib.auth.backends.ModelBackend',
]

LOGIN_URL = 'account/login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'
# LOGOUT_REDIRECT_URL = 'account/login'

# SOCIAL_AUTH_FACEBOOK_KEY='858995061590537'
# SOCIAL_AUTH_FACEBOOK_SECRET = 'b6c1cd4a7c1d6461b00fbdf268687e65'

SOCIAL_AUTH_GITHUB_KEY='873a9787fcdaf0c0f4f7'
SOCIAL_AUTH_GITHUB_SECRET='221ebf833785aeefeadd28763ddab7205024bd83'

# SOCIAL_AUTH_TWITTER_KEY=''
# SOCIAL_AUTH_TWITTER_SECRET=''

# SOCIAL_AUTH_GOOGLE_KEY=''
# SOCIAL_AUTH_GOOGLE_SECRET=''

SITE_ID=1

MAPBOX_KEY = "pk.eyJ1IjoiYXJ1bjYzNjQiLCJhIjoiY2tqNzFvbzg1NmYybDJ4cWpueGNwNmRneCJ9.ViyuoINx3lLERUsD9Hswlw"

# Ckeditor config
CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'

def blog_body_images_directory_path(instance, filename):
    return 'user_{0}/blog/{1}/body_images/{2}'.format(instance.author.id, instance.title, filename)

CKEDITOR_UPLOAD_PATH = blog_body_images_directory_path
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': None,
    },
}