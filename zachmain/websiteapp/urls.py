from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "websiteapp"
urlpatterns = [
    path(
        "",
        TemplateView.as_view(template_name="pages/about.html"),
        name="about-us",
    ),
    path("vision/", views.website_page, name="vision"),
    path("what-we-do/", views.whatwedo_page, name="what-we-do"),
    path("gallery/", views.gallery_view, name="gallery"),
    path("leadership/", views.leadership_view, name="leadership"),
    path("contacts/", views.contacts_page, name="contacts"),
]
