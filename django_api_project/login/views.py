from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import SignUpForm


# Create your views here.

def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')  # Replace 'home' with your home page URL name
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
