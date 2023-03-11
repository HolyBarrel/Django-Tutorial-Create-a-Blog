from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('articles:list')
    else:
        form = UserCreationForm()
    
    #occurrs finally if there is a get-request or the post-request was sent on an invalid form
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('articles:list')

    else: 
        form = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'form': form})