from django.urls import path
from .views import job_list, job_detail

app_name = "careers"

urlpatterns = [
    path("", job_list, name="list"),
    path("<int:pk>/", job_detail, name="detail"),
]