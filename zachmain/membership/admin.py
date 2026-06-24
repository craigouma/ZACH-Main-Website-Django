from django.contrib import admin

from .models import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Member model.
    Includes list display, search, filters, and a custom action to deactivate members.
    """

    list_display = ["name", "phone", "bed_band", "is_active", "created_at"]
    list_filter = ["is_active", "bed_band"]
    search_fields = ["name", "address", "phone"]
    actions = ["deactivate_members", "activate_members"]

    # Custom action to deactivate members (e.g., for unpaid subscriptions)
    @admin.action(description="Deactivate selected members (Unpaid Subscriptions)")
    def deactivate_members(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(
            request, f"{updated} members were successfully marked as inactive."
        )

    # Custom action to activate members
    @admin.action(description="Activate selected members (Subscription Paid)")
    def activate_members(self, request, queryset):
        updated = queryset.update(is_active=True)
        self.message_user(
            request, f"{updated} members were successfully marked as active."
        )
