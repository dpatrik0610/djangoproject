from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

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

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'website/dashboard.html')
