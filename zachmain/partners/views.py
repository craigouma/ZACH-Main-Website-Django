from django.shortcuts import render

from .models import Partner


def partners_view(request):
    partners = Partner.objects.all()
    return render(request, "partners/slider.html", {"partners": partners})
