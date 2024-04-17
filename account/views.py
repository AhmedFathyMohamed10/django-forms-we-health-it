from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import UserRegisterForm, UserLoginForm, ProfileForm
from .models import Profile

# Create your views here.

def register(request):
    form = UserRegisterForm()  # Instantiating the form
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)  # <-- Problematic line
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)
            profile.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegisterForm()  # This line is redundant

    return render(request, 'register.html', {'form': form})
def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Assuming 'home' is the name of your home page URL
            else:
                # Authentication failed
                form.add_error(None, 'Invalid username or password')
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('home')


def profile(request):
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return HttpResponse('Invalid form')
    else:
        form = ProfileForm()
    return render(request, 'profile.html', {'form': form})