from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from . import forms


def user_login(request):
    if request.user.is_authenticated:
        return redirect('home_app:home')

    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request, user)
            return redirect('home_app:home')
    else:
        form = forms.LoginForm()
    return render(request, 'account/login.html', {'login_form': form})


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect('home_app:home')


def user_register(request):
    if request.user.is_authenticated:
        return redirect('home_app:home')

    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username, password=password)

            login(request, user=User.objects.get(username=username))

            return redirect('home_app:home')
    else:
        form = forms.RegisterForm()
    return render(request, 'account/register.html', {'register_form': form})
