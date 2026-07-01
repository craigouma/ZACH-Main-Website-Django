from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import Programme


def programme_list(request):
    """
    Displays a list of all programmes using a Function-Based View (FBV).

    The programmes are fetched from the database and ordered by
    active status (active first) and then by name.
    """
    programmes = Programme.objects.filter(is_active=True).order_by("name")
    context = {
        "programmes": programmes,
    }
    return render(request, "programmes/landing_page.html", context)


def programme_detail(request, pk):
    """
    Displays the full description and details for a single Programme.

    Uses get_object_or_404 to handle cases where the primary key (pk) is invalid.
    """
    programme = get_object_or_404(Programme, pk=pk)
    context = {
        "programme": programme,
    }
    return render(request, "programmes/programme_detail.html", context)
