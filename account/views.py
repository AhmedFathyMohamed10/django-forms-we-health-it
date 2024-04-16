from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import authenticate, login

def register(request):
    form = UserRegisterForm()  # Instantiating the form
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)  # <-- Problematic line
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
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

