from django.urls import path
from . import views

app_name = "reports"

urlpatterns = [
    path("export/", views.export_report, name="export"),
]