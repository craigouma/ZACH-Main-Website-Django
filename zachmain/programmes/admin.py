from django.contrib import admin

from .models import Programme


@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Programme model.
    """

    list_display = ["name", "is_active", "photo_tag"]
    list_filter = ["is_active"]
    search_fields = ["name", "description"]
    actions = ["make_active", "make_inactive"]

    @admin.display(
        description="Photo Uploaded",
    )
    def photo_tag(self, obj):
        """Displays a small image in the admin list."""
        if obj.photo:
            # Requires 'from django.utils.html import format_html' if used for image display
            # But for list_display, just checking existence is fine.
            return "Yes"
        return "No"

    # Custom action to set programmes as active
    @admin.action(description="Mark selected programmes as active")
    def make_active(self, request, queryset):
        updated = queryset.update(is_active=True)
        self.message_user(
            request, f"{updated} programmes were successfully marked as active."
        )

    # Custom action to set programmes as inactive
    @admin.action(description="Mark selected programmes as inactive")
    def make_inactive(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(
            request, f"{updated} programmes were successfully marked as inactive."
        )
