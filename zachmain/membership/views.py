from django.shortcuts import render
from django.db.models import Q
from .models import Member

def member_list_and_search(request):
    """
    Lists all members and handles member searching by name, address, or phone.
    Member creation and deactivation must now be performed exclusively 
    via the Django Admin interface.
    """
    query = request.GET.get('q')
    # Order by active status (active first) and then by name
    members = Member.objects.all().order_by("-is_active", "name")

    if query:
        # Search members using Q objects for OR logic
        members = members.filter(
            Q(name__icontains=query) |
            Q(address__icontains=query) |
            Q(phone__icontains=query)
        ).distinct()

    context = {
        'members': members,
        'query': query,
    }
    return render(request, 'membership/member_list.html', context)


def membership_benefits(request):
    return render(request, "membership/benefits.html")

def howtojoin(request):
    return render(request, "membership/how-to-join.html")
