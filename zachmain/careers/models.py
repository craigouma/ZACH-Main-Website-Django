from django.db import models
from model_utils.models import TimeStampedModel

class JobListing(TimeStampedModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=100)
    
    # New Fields
    closing_date = models.DateTimeField(
        help_text="The date and time when the advert will expire."
    )
    application_link = models.URLField(
        max_length=500,
        help_text="The external link (e.g., LinkedIn or Google Forms) for submissions."
    )
    
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created"] # Newest adverts first

    def __str__(self):
        return self.title
# Create your models here.
