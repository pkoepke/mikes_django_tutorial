"""
Django settings for django_test project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'tcp^^i-0v&+yg$2ls#6dfyxqm#qzd0i=e70y&)z2!z1#d%b_@*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

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
    'article',
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

ROOT_URLCONF = 'django_test.urls'

WSGI_APPLICATION = 'django_test.wsgi.application'

TEMPLATE_DIRS = (
    # relative paths are not allowed, but you can use BASE_DIR to do the same thing
    os.path.join(BASE_DIR, 'templates'),
#    os.path.join(BASE_DIR, '/article/templates'),
)

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'America/Detroit'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

# Tutorial had STATIC_ROOT = '', but that wasn't working for me.
STATIC_ROOT = '/home/paul/Programming/mikes_django_tutorial/mikes_intro_to_django/django_test/static/'

# This is what the tutorial asked for, and it worked.
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    ('assets', os.path.join(BASE_DIR, 'static/assets') ), # /static/assets didn't work, it has to be static/assets without the leading slash.
    # Also, the tutorial left out the /assets/ part, but that caused an error when running 'python manage.py collectstatic': "django.core.exceptions.ImproperlyConfigured: The STATICFILES_DIRS setting should not contain the STATIC_ROOT setting"
)
