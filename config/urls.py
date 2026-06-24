from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path, re_path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.views.static import serve # Add this import
import re

# Customise Django portal
admin.site.site_header = "ZACH Administration Portal"
admin.site.site_title = "ZACH Admin Portal"
admin.site.index_title = "Welcome to ZACH Website Content Management System"

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("zachmain.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
    path("membership/", include("zachmain.membership.urls", namespace="membership")),
    path("about-us/", include("zachmain.websiteapp.urls", namespace="websiteapp")),
    path("news/", include("zachmain.news.urls")),
    path("programmes/", include("zachmain.programmes.urls", namespace="programmes")),
    path("partners/", include("zachmain.partners.urls", namespace="partners")),
    path("careers/", include("zachmain.careers.urls", namespace="careers")),
     # Third-party URLS
    path("ckeditor5/", include("django_ckeditor_5.urls")),
    # ...
    # Legacy URL redirects (301) so old bookmarks/links keep working
    path("about/", RedirectView.as_view(url="/about-us/", permanent=True)),
    path("aboutus/", RedirectView.as_view(url="/about-us/", permanent=True)),
    path("aboutus/vision/", RedirectView.as_view(url="/about-us/vision/", permanent=True)),
    path("aboutus/whatwedo/", RedirectView.as_view(url="/about-us/what-we-do/", permanent=True)),
    path("aboutus/gallery/", RedirectView.as_view(url="/about-us/gallery/", permanent=True)),
    path("aboutus/leadership/", RedirectView.as_view(url="/about-us/leadership/", permanent=True)),
    path("aboutus/contacts/", RedirectView.as_view(url="/about-us/contacts/", permanent=True)),
    path("partner/", RedirectView.as_view(url="/partners/", permanent=True)),
    # Media files
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [
            path("__debug__/", include(debug_toolbar.urls)),
            *urlpatterns,
        ]
