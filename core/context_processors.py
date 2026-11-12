from django.conf import settings


def features(request):
    return {"ENABLE_REPORTS": settings.ENABLE_REPORTS}