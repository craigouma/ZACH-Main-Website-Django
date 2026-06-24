from .models import Article


def latest_articles(request):
    return {
        "latest_articles": Article.objects.order_by("-created_at")[:5],
    }
