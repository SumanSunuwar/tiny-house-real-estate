from .base import *

DATABASES = {
    'default': {
        'ENGINE': env("POSRGRES_ENGINE"),
        'NAME': env("POSTGRES_DB"),
        'USER': env("POSTGRES_PASSWORD"),
        'PASSWORD': env("POSTGRES_PASSWORD"),
        'HOST': env("PG_HOST"),
        'PORT': env("PG_PORT"),
    }
}