from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden

# Views

def index(request):
    if request.user.is_authenticated:
        return render(request, 'website/index.html', {'authenticated': True})
    else:
        return render(request, 'website/index.html', {'authenticated': False})

def home(request):
    return render(request, 'website/home.html')

def items(request):
    return render(request, 'website/items.html')

def menu(request):
    return render(request, 'website/menu.html')
