from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse

from app.models import Contact
# Create your views here.
def Home(request):
    return render(request,"Home.html")

def gallery(request):
  
    return render(request,"gallery.html")

def karnataka(request):
  
    return render(request,"karnataka.html")

def kerala(request):
  
    return render(request,"kerala.html")

def maharashtra(request):
  
    return render(request,"maharashtra.html")

def tamilnadu(request):
  
    return render(request,"tamilnadu.html")


def contact(request):
   
    return render(request,"contact.html")



      