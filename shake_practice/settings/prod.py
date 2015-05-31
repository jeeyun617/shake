from .common import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '',
        'NAME': 'shake_db',
        'USER': 'shake',
        'PASSWORD': '',
    }
}
