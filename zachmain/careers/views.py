from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import JobListing

def job_list(request):
    """
    Displays all active jobs that haven't reached their closing date.
    """
    jobs = JobListing.objects.filter(
        is_active=True,
        closing_date__gt=timezone.now()
    ).order_by("-created")
    
    context = {
        "jobs": jobs,
    }
    return render(request, "careers/job_list.html", context)

def job_detail(request, pk):
    """
    Displays a single job's details.
    """
    job = get_object_or_404(JobListing, pk=pk, is_active=True)
    
    context = {
        "job": job,
    }
    return render(request, "careers/job_detail.html", context)
