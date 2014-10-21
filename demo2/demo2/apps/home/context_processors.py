from django.conf import settings as _settings
import django

def settingss(request):
	
    # los devolvemos en la variable de contexto "settings"
    return {'settings': _settings}


def django_version(request):
    return { 'django_version': django.VERSION }