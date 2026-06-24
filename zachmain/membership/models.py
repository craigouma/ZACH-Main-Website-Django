from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Member(models.Model):
    """
    Model for managing organizational members (e.g., hospitals, clinics).
    """
    
    # Bed size bands as requested by the user
    BED_BAND_CHOICES = (
        ('0-50', _('0 - 50 Beds')),
        ('51-100', _('51 - 100 Beds')),
        ('101+', _('101+ Beds')),
    )

    name = models.CharField(
        _("Member Name (Organization/Hospital)"), 
        max_length=255
    )

    website = models.URLField(
        _("Website Address"),
        max_length=200,
        blank=True,
        null=True,
        help_text=_("The official website URL (e.g., https://www.hospital.com)"),
    )
    
    address = models.TextField(
        _("Physical Address"),
        help_text=_("The official physical address of the member.")
    )

    phone = models.CharField(
        _("Contact Phone Number"), 
        max_length=50,
        blank=True,
        null=True
    )

    bed_band = models.CharField(
        _("Number of Beds Band"),
        max_length=10,
        choices=BED_BAND_CHOICES,
        default='0-50'
    )

    is_active = models.BooleanField(
        _("Is Active (Subscription Paid)"), 
        default=True,
        help_text=_("Designates whether this member is currently active (subscriptions paid).")
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = _("Member")
        verbose_name_plural = _("Members")
        # Order by active status first (inactive members float to the bottom of the list/admin)
        ordering = ["-is_active", "name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # Redirect to the list view after save/edit
        return reverse("membership:list")