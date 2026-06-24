from django.contrib import admin

from .models import GalleryImage
from .models import Leader
from .models import Resource


@admin.register(Leader)
class LeaderAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "order")
    list_editable = ("order",)


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ("title", "published_date", "file", "external_url")
    search_fields = ("title", "description")


admin.site.register(GalleryImage)

# Register your models here.
