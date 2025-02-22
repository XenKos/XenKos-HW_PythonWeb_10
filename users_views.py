from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm

def signupuser(request):
    if request.user.is_authenticated:
        return redirect('home')  

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'users/signup.html', {'form': form})