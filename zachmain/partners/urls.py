from django.urls import path

from . import views

app_name = "partners"
urlpatterns = [
    path("", views.partners_view, name="partner"),
]
