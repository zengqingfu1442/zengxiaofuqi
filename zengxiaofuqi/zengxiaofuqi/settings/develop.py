from .base import *   # NOQA


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'USER': 'root',
        'PASSWORD': '',
        'PORT': '3306',
        'NAME': 'zengxiaofuqi_db',
        'TEST': {
            'NAME': 'test_zengxiaofuqi_db',
        }
    }
}