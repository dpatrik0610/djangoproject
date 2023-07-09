from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import CreateUserForm

'''Login'''
def loginPage(request):
    if is_logged_in(request.user):
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                messages.success(request, f'User {username} logged in.')
                return redirect('index')
            else:
                messages.info(request, f'Username or password is incorrect.')
            
        context = {}
        return render(request, 'accounts/login.html', context=context)

'''Register'''
def registerPage(request):
    if is_logged_in(request.user):
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for: '+ username)
                return redirect('login')
            else:
                messages.error(request, "Something went wrong.")
            
        context = {"form": form}
        return render(request, 'accounts/register.html', context=context)

'''Logout'''
def logoutUser(request):
    logout(request)
    return redirect('index')

def is_logged_in(user):
    return user.is_authenticated
