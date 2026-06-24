from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field


class Programme(models.Model):
    """
    Model for managing educational or community programmes.
    """

    # Simple title for the programme
    name = models.CharField(
        _("Programme Name"),
        max_length=255,
        unique=True,
    )

    # Stores the rich text description.
    # NOTE: For "bold or underline" ability, you will need to install
    # a package like 'django-ckeditor' or 'django-tinymce' and replace
    # models.TextField with the package's RichTextField.
    description = CKEditor5Field("Text", config_name="extends")
    # Photo/Image for the programme
    photo = models.ImageField(
        _("Programme Photo"),
        upload_to="programmes/photos/",
        null=True,
        blank=True,
    )

    # Status to show if the programme is active or not
    is_active = models.BooleanField(
        _("Is Active"),
        default=True,
        help_text=_("Designates whether this programme should be treated as active."),
    )

    class Meta:
        verbose_name = _("Programme")
        verbose_name_plural = _("Programmes")
        ordering = ["-is_active", "name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # Assuming you will eventually create a detail view
        return reverse("programmes:detail", kwargs={"pk": self.pk})


# Create your models here.
