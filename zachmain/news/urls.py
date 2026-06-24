from django.urls import path

from . import views

app_name = "news"

urlpatterns = [
    path("<slug:slug>/", views.article_detail, name="article_detail"),
    path("", views.newsletter, name="newsletter"),
]
