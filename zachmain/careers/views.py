from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import JobListing

def job_list(request):
    jobs = JobListing.objects.filter(is_active=True).order_by("-created")
    context = {
        "jobs": jobs,
    }
    return render(request, "careers/job_list.html", context)

def job_detail(request, pk):
    job = get_object_or_404(JobListing, pk=pk, is_active=True)
    
    context = {
        "job": job,
    }
    return render(request, "careers/job_detail.html", context)
