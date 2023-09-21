from django.shortcuts import render, redirect
from django.contrib.auth import login
from main.forms import SignUpForm

# Create your views here.


def index(request):
    return render(request, 'main/index.html')

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    form = SignUpForm()
    return render(request, 'main/signup.html', {'form': form})
