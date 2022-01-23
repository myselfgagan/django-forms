from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import contacts
from django.contrib import messages  

# Create your views here.
def index(request):
    context = {
        "variable" : "this is variable sent"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is home page")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is about page")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("This is services page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        desc = request.POST.get("desc")
        contact = contacts(name = name, email = email, desc = desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your query is submitted')

    return render(request, 'contact.html')
    # return HttpResponse("This is contact page")