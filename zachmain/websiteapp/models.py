from django.db import models


class GalleryImage(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to="gallery/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Image {self.id}"


class Leader(models.Model):
    NAME_CHOICES = [
        ("ZHOD", "ZHoCD"),
        ("CHAIR", "Board Chairperson"),
        ("BOARD", "Board Member"),
        ("ED", "Executive Director"),
        ("PM", "Program Manager"),
        ("FAM", "Finance & Admin Manager"),
    ]

    name = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=NAME_CHOICES)
    photo = models.ImageField(upload_to="leadership/")
    bio = models.TextField(blank=True, default="")
    order = models.PositiveIntegerField(
        default=0, help_text="Lower numbers appear higher up."
    )

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.name} - {self.get_role_display()}"


class Resource(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to="resources/", blank=True)
    external_url = models.URLField(max_length=500, blank=True)
    published_date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-published_date"]
