from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from templates import *
from .forms import *
from .models import *

# Create your views here.
def user_register(request):
    if request.method == 'POST':
        if UserAuth.objects.filter(email=request.POST.get('email')):
            alert = True
            return render(request, 'register.html', {'alert' : alert})
        else:
            UserPassword = request.POST.get('password')
            if len(UserPassword) < 6:
                return redirect('/register')
            else:
                uppercase = 0
                lowercase = 0
                digit = 0
                special = 0
                regex = "@_!#$%^&*()<>?/|}{~:]"
                for n in UserPassword:
                    if n.isupper():
                        uppercase += 1
                    elif n.islower():
                        lowercase += 1
                    elif n.isdigit():
                        digit += 1
                    elif n in regex:
                        special += 1
                    else:
                        return redirect('/register')
                if (uppercase>0 and lowercase>0) and (digit>0 and special>0):
                    newuser = UserAuth.objects.create(
                        email = request.POST.get('email'),
                        name = request.POST.get('name'),
                        message = request.POST.get('message')
                    )
                    newuser.password = set_password(UserPassword)
                    newuser.save()
                    return redirect('/login')
                else:
                    return redirect('/register')
    return render(request, 'register.html')


def user_login(request):
    alert = False
    if request.method == 'POST':
        userEmail = request.POST.get('email')
        userPassword = request.POST.get('user_password')
        user = authenticate(request, email=userEmail, password=userPassword)
        if user is not None:
            return render(request, 'home.html', {'user' : user})
        else:
            alert = True
            return render(request, 'login.html', {'alert': alert})

    return render(request, 'login.html')


def user_home(request):
    return render(request, 'home.html')