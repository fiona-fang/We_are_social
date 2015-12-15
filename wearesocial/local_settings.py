from settings import INSTALLED_APPS, BASE_DIR
import os


DEBUG = True

# INSTALLED_APPS += ('debug_toolbar',)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

TEMPLATE_DEBUG = True

STATIC_ROOT = (os.path.join(BASE_DIR, 'static'),)



