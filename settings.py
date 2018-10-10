# coding: utf-8

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = os.environ.get('LEANCLOUD_APP_ENV') != 'production'
ROOT_URLCONF = 'urls'
SECRET_KEY = 'replace-this-with-your-secret-key'
ALLOWED_HOSTS = ['*']

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': ['templates'],
}]

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


LC_APP_ID = 'DQ5Ny*************zGzoHsz'
LC_APP_KEY = 'TYn*********bm5Nt'
LC_APP_MASTER_KEY = '6bBFh**********j7ez4di'
