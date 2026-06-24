from django.shortcuts import render

from .models import GalleryImage
from .models import Leader


def leadership_view(request):
    leaders = Leader.objects.all()
    # Categorizing them for easy layout in the template
    context = {
        "zhod": leaders.filter(role="ZHOD"),
        "chair": leaders.filter(role="CHAIR"),
        "board": leaders.filter(role="BOARD"),
        "ed": leaders.filter(role="ED"),
        "managers": leaders.filter(role__in=["PM", "FAM"]),
    }
    return render(request, "websiteapp/leadership.html", context)


def gallery_view(request):
    images = GalleryImage.objects.all().order_by("-created_at")
    return render(request, "websiteapp/gallery.html", {"images": images})


def website_page(request):
    return render(request, "websiteapp/vision.html")


def vision_page(request):
    return render(request, "websiteapp/vision.html")


def whatwedo_page(request):
    return render(request, "websiteapp/what-we-do.html")


def contacts_page(request):
    return render(request, "websiteapp/contacts.html")
