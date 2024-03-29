from django.shortcuts import render, redirect
from . forms import DataForm
from . models import Data

# Create your views here.

def data(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-predictions')
    else:    
        form = DataForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/data.html', context)

def predictions(request):
    shortlisted_applicants = Data.objects.all()
    context = {
        'shortlisted_applicants': shortlisted_applicants
    }
    return render(request, 'dashboard/predictions.html', context)

