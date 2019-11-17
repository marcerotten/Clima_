from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return render(request, "core/home.html")

def index(request):
    return render(request, "core/index.html")

def statistics(request):
    return render(request, "core/statistics.html")

def register(request):
    return render(request, "core/register.html")

def contact(request):
    return render(request, "core/contact.html")

def navbar(request):
    return render(request, "core/navbar.html")

