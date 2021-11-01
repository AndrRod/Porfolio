from pathlib import Path
from whitenoise import WhiteNoise



import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-g1okie^%-_gzb#idh#gxlw*wpy^9_nxbj=s-twzvyu5#4%i2u2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    # 31/10
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Portafolio',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     AGREGAMOS WHITENOSE PARA HEROKU

]

MIDDLEWARE_CLASSES = (
    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/
    'whitenoise.middleware.WhiteNoiseMiddleware',
    )

ROOT_URLCONF = 'Portafolio.urls'
import os

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'Portafolio/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI_APPLICATION = 'Portafolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# 31/10
import dj_database_url
from decouple import config
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )

}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2', # Aca agregamos postgresql
#         # 'NAME': 'MultipleChoice',
#         'USER': 'postgres',
#         'PASSWORD': 'Lgante03',
#         'HOST': '127.0.0.1',
#         'DATABASE_PORT': '5432',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

   

import os
import django_heroku

# SECRET_KEY = "es_un_secreto"

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))




django_heroku.settings(locals())   
    
    

#31/10 DJANGO NO SOPORTA ARCHIVOS STATICOS EN PRODUCCION 

STATICFILES_DIRES = (os.path.join(BASE_DIR, 'static'),)
# STATICFILES_DIRES = [
#     BASE_DIR 'static',
#     BASE_DIR / 'Portafolio' /'static',
#     BASE_DIR / 'Portafolio' / 'Portafolio' /'static',
#     BASE_DIR / 'app' / 'static', 
    
    
# ]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'





# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# 1/11

SEND_BROKEN_LINK_EMAILS=True

EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'


EMAIL_HOST="smtp.gmail.com" #HAY QUE ESPECIFICAR EL HOST: parametros de gmail en este caso, # tambien hay que configurar el gmial personal para poder usarlo para recibir correos
# deshabilitar Acceso de aplicaciones poco seguras, porque gmail viene por defecto la prohibición de terceros (Acceso de aplicaciones poco seguras)

EMAIL_USE_TLS=True
EMAIL_USE_SSL=False
#especificar protocolos para enviar el correo o parametros

EMAIL_PORT=587
#Es el puerto de gmail
EMAIL_HOST_USER="rodrigueza.federacion@gmail.com"
EMAIL_HOST_PASSWORD="Cucaracha09"





STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = "/static/"
STATIC_DIR = (os.path.join(BASE_DIR, "/static"),)