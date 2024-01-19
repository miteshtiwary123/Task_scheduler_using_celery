"""Views for celery app."""
from django.shortcuts import render, redirect
from .forms import SoftwareDetailsForm
from .models import SoftwareDetails

def create_form(request):
    """Function to create form"""
    if request.method == 'POST':
        form = SoftwareDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_data')
    else:
        form = SoftwareDetailsForm()

    return render(request, 'create_form.html', {'form': form})

def display_data(request):
    """Function to display data."""
    data = SoftwareDetails.objects.all()
    return render(request, 'display_data.html', {'data': data})
