"""
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
import os
import sys
from os.path import join, abspath, dirname


here = lambda *x: join(abspath(dirname(__file__)), *x)
PROJECT_ROOT = here('..', '..')
root = lambda *x: join(abspath(PROJECT_ROOT), *x)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!6)1f%0tqv12rf*kj=k89w3(mm)89_smq@%2p54@0j$d392_up'



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*',]

ADMINS = (
    ('Komu Wairagu', 'komuw05@gmail.com'),
)

# Application definition
DEFAULT_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = ('south', 'django_extensions',)

LOCAL_APPS = ( 'sample_app',)

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': root('db.sqlite3'),
    }
}

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Nairobi'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = root('static/')
STATIC_URL = '/static/'

MEDIA_ROOT = root('media/')
MEDIA_URL = '/media/'

LOGGING = {
    'version': 1,
}




##########################
## some useless stuff
##########################

# <script src="{% static 'main/js/jquery.js' %}"></script>
        
#  <script>
#    $(document).ready(function()
#     {
#        switch (document.location.pathname) {
#        case "/about":
#           alert("You entered p1!");
#           $("#about_us_menu").addClass("active");
#           break;
#        case "/contact":
#           $("#contact_menu").addClass("active");
#           break;
#        case "/main/":
#           $("#ward_menu").addClass("active");
#           break;
#        default:
#           $("#home_menu").addClass("active");
#         }
#     }
# );