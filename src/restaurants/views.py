from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "home.html", {'var': 'tutorial'})

def about(request):
    context = {}
    return render(request, "about.html", context)

def contact(request):
    context = {}
    return render(request, "contact.html", context)