from django.conf import settings


def features(request):
    return {
        "ENABLE_REPORTS": settings.ENABLE_REPORTS,
        "ENABLE_NOTIFICATIONS": settings.ENABLE_NOTIFICATIONS,
        "PRODUCT": settings.PRODUCT,
    }