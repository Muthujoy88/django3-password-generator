from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
import random

# Create your views here.

def home(request):
    return render(request,'generator/home.html',{'Password':'test123h'})

def password(request):
    length = int(request.GET.get('length'))
    characters = list('abcdefghijklmnopqrstuvwxyz')
    thepassword=''
    for x in range(length):
        thepassword += random.choice(characters)
    
    return render(request,'generator/password.html',{'pass':thepassword})

def about(request):
    return render(request,'generator/about.html')