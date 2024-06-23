from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserLoginForm, AuthorForm, QuoteForm
from .models import Author, Quote

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to appropriate page after adding author
    else:
        form = AuthorForm()
    return render(request, 'add_author.html', {'form': form})

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to appropriate page after adding quote
    else:
        form = QuoteForm()
    authors = Author.objects.all()
    return render(request, 'add_quote.html', {'form': form, 'authors': authors})

def author_detail(request, author_id):
    author = Author.objects.get(id=author_id)
    quotes = author.quotes.all()
    return render(request, 'author_detail.html', {'author': author, 'quotes': quotes})


