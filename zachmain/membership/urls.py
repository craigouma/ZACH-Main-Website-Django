from django.urls import path
from .views import member_list_and_search, membership_benefits, howtojoin

app_name = "membership"
urlpatterns = [
    # List and Search View: /membership/
    path("", member_list_and_search, name="list"),
    path("benefits/", membership_benefits, name="benefits"),
    path("how-to-join/", howtojoin, name="how-to-join")
    # Member creation and deactivation are now handled ONLY in Django Admin.
]
