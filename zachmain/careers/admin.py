from django.contrib import admin
from .models import JobListing

@admin.register(JobListing)
class JobListingAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "closing_date", "is_active")
    list_filter = ("is_active", "created")
    search_fields = ("title", "description")

# Register your models here.
