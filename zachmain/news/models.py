from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="articles/")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Newsletter(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=500)
    published_date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-published_date"]
