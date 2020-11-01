from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

def home(request):
    user = request.user
    if user.is_authenticated:
        return redirect("/home")
        
    return render(request, 'index.html')

def home_logado(request):
    return render(request, 'home.html')