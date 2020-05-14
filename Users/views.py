from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .forms import NewUserForm

# Create your views here.
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out succesfully!")
    return redirect("/")

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                print(form.errors)
        else:
            print(form.errors)
    form = AuthenticationForm()

    context = {
        "form": form
    }
    return render(request, "users/login.html", context)

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "Account Registered Succesfully")
                return redirect('/')
            else:
                print(form.errors)
        else:
            print(form.errors)
    form = UserCreationForm()

    context = {
        "form": form
    }
    return render(request, "users/register.html", context)



























































































#def user_login_view(request):
#    username = "username" in request.POST
#    password = "password" in request.POST
#    user = authenticate(request, username = username, password = password)
#    if user is not None:
#        login(request, user)
#        return render(request, "Templates/home_page.html", {})
#    else:
#        print("Enter a valid username and password.")
#
#    context = {
#        "user" : user
#    }
#    return render(request, "users/login.html", context)
