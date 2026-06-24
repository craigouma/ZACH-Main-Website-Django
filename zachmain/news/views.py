from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import Article


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, "news/article_detail.html", {"article": article})


def newsletter(request):
    return render(request, "news/newsletter.html")
