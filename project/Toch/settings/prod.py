from .base import *

ALLOWED_HOSTS = ['toch.co.kr', 'toch.kr', 'm.toch.kr']
DEBUG = False

BASE_DIR = Path(__file__).resolve().parent.parent
ROOT_DIR = os.path.dirname(BASE_DIR)

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

STATIC_ROOT = os.path.join(ROOT_DIR, '.static_root')
