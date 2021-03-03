from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.

def view_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #login
            #login(request, user)
            return redirect('accounts:login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html' , {'form' : form})

def view_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            #login
            user = form.get_user()
            login(request, user)
            return redirect('chart:create')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form' : form})

def view_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:login')
