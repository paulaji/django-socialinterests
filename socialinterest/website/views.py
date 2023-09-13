from django.shortcuts import render, redirect
from .forms import AddNewLead
from .models import NewLead
from django.contrib import messages


# Create your views here.
def home(request):
    # Retrieve all new lead records
    newleads = NewLead.objects.all()
    return render(request, 'home.html', {'newleads': newleads})

# to add new leads  
def add_newlead(request):
    if request.method == "POST":
        form = AddNewLead(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New Lead added successfully!")
            return redirect('home')
        else:
            messages.error(request, "Form submission failed. Please check the data you entered.")
    else:
        form = AddNewLead()
    return render(request, "add_newlead.html", {'form': form})
