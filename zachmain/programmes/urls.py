from django.urls import path
from django.views.generic import RedirectView

from . import views

app_name = "programmes"
urlpatterns = [
    path("", RedirectView.as_view(url="/programmes/landing/", permanent=False)),
    path("landing/", views.programme_list, name="programmes_page"),
    path("<int:pk>/", views.programme_detail, name="detail"),
]
