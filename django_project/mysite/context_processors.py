from django.conf import settings


def sitename(request):
    return {
        'SITENAME': settings.SITENAME
    }
