from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.views.decorators.cache import never_cache
from .middlewares import *
from templates import *
from .forms import *
from .models import *


# Create your views here.
def user_register(request):
    if request.method == 'POST':
        if UserAuth.objects.filter(email=request.POST.get('email')):
            return render(request, 'register.html', {'alert' : True})
        else:
            userpassword = request.POST.get('password')
            special_char = ['/', '[', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ',', '.', '?', ':', '{', '}', '|', '<', '>', ']']
            if len(userpassword) < 8:
                return render(request, 'register.html', {'error' : True})
            elif " " in userpassword.strip():
                return render(request, 'register.html', {'error' : True})
            else:
                upper_flag = 0
                lower_flag = 0
                digit_flag = 0
                special_flag = 0
                for char in userpassword:
                    if char in special_char:
                        special_flag += 1
                        continue
                    elif char.isdigit():
                        digit_flag += 1
                        continue
                    elif char.islower():
                        lower_flag += 1
                        continue
                    elif char.isupper():
                        upper_flag += 1
                        continue
                    else:
                        continue
                    
                if (upper_flag == 0 or lower_flag == 0) or (digit_flag == 0 or special_flag == 0):
                    return render(request, 'register.html', {'error': True})
                    
                else:
                    newuser = UserAuth.objects.create(
                        email = request.POST.get('email'),
                        name = request.POST.get('name'),
                        message = request.POST.get('message')
                    )
                    newuser.password = set_password(userpassword)
                    newuser.save()
                    return render(request, 'register.html', {'success' : True})
    else:
        success_message = False
        error_message = False
        return render(request, 'register.html', {'success':success_message, 'error': error_message})


@user_login
@never_cache
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                request.session['auth_token'] = 'login'
                request.session['user'] = user.email
                return redirect('home')
            else:
                request.session['auth_token'] = None
                return render(request, 'login.html', {'alert': True, 'form': form})
        else:
            return render(request, 'login.html', {'from': form})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'alert': False, 'form': form})


@user_logout
@never_cache
def user_home(request):
    useremail = request.session.get('user')
    user = UserAuth.objects.get(email = useremail)
    return render(request, 'home.html', {'user': user})


def user_signout(request):
    request.session['auth_token'] = 'logout'
    return redirect('login')
