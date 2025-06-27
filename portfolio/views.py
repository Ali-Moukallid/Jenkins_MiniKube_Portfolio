from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, CollaborationRequest
from .forms import CollaborationForm

def home(request):
    return render(request, 'portfolio/home.html')

def current_work(request):
    projects = Project.objects.all().order_by('-date_added')
    return render(request, 'portfolio/current_work.html', {'projects': projects})

def collaborate(request):
    if request.method == 'POST':
        form = CollaborationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your collaboration request has been submitted successfully!')
            return redirect('collaborate')
    else:
        form = CollaborationForm()
    return render(request, 'portfolio/collaborate.html', {'form': form})

def admin_dashboard(request):
    collaboration_requests = CollaborationRequest.objects.all().order_by('-submission_date')
    return render(request, 'portfolio/admin_dashboard.html', {'requests': collaboration_requests}) 