from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return render(request, "about.html")
    #return HttpResponse("about")

def home(request):
    return render(request, "home.html")
    #return HttpResponse("home")
   