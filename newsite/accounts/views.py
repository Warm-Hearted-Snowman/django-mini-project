from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout


# Create your views here.
def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'], cd['email'], cd['password'])
            messages.success(request, f"{cd['username']} registered successfully", 'success')
            return redirect('users')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, f"{cd['username']} logged in successfully", 'success')
                return redirect('users')
            else:
                messages.error(request, 'Wrong username or password', 'danger')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def logout_user(request):
    print(request.user)
    if request.user.id is not None:
        messages.success(request, f"'{request.user}' logged out successfully", 'success')
        logout(request)
    else:
        messages.error(request, f'You were not logged in', 'danger')
    return redirect('users')
