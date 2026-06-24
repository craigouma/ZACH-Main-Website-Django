from django.contrib import admin

from .models import Article
from .models import Newsletter


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ("title", "published_date", "url")
    search_fields = ("title",)
