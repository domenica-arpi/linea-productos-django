from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
]

if settings.ENABLE_REPORTS:
    urlpatterns += [path("reports/", include("reports.urls"))]