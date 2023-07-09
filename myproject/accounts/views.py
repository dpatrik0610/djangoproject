from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

def loginPage(request):
    context = {}
    return render(request, 'accounts/login.html', context=context)

def registerPage(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {"form": form}
    return render(request, 'accounts/register.html', context=context)