from .base import *

ALLOWED_HOSTS = ['114.70.93.100', 'toch.co.kr', 'toch.kr']
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Toch',
        'USER': 'root',
        'PASSWORD': 'cheese215',
        'HOST': '192.168.0.93',
        'PORT': '3306',
    }
}
