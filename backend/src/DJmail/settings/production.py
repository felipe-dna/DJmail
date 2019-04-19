from .base import *


# Leia esta documentação antes de fazer deploy da aplicação.
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/


ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
# => Configurações do banco de dados devem ser setadas em variáveis ambiente.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # se vc estiver utilizando postgresql
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': '',
    }
}
