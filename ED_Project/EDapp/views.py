from django.shortcuts import render, redirect
from EDapp.models import userlogin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def userlogout(request):
    userid = request.session.get('user')
    pwd = request.session.get('pwd')
    
    user = authenticate(username=userid, password=pwd)
    logout(request)
    return redirect('/login')

def Login(request):
    if request.method == 'POST':
        Username = request.POST.get('username')
        Password = request.POST.get('password')
        
        request.session['user'] = Username
        request.session['pwd'] = Password

        user = authenticate(username=Username, password=Password)

        if user is not None: 
            login(request, user)
            return redirect("home")
        else:
            return render(request, 'login.html')
    
    return render(request, 'login.html')

def home(request):
    return render(request, "home.html")
   
def encoder(request):
    if request.method == "POST":
        E_userInput = request.POST.get('E_userinput')
        E_userInput += "."
        str = ""
        E_Output = ""
        for i in E_userInput:
            if i == " " or i == E_userInput[len(E_userInput) - 1]:
                if len(str) <= 3:
                    E_Output += str[::-1] + " "
                    str = ""
                elif len(str) > 6:
                    for repeat in range(2):
                        val = str[:4]
                        str = str.replace(str[:4], "", 1)
                        str += val
                    E_Output += str[::-1] + " "
                    str = ""
                else:
                    val = str[1]
                    str = str.replace(str[1], "", 1) 
                    str = str + val
                    E_Output += str[::-1] + " "
                    str = ""
            else:
                str += i
                
        return render(request, 'encoder.html', {'E_Output': E_Output})
    
    else:
        return render(request, 'encoder.html')
    
def decoder(request):
    if request.method == "POST":
        D_userInput = request.POST.get('D_userinput')
        D_userInput += "."
        D_Output = ""
        str = ""
        for i in D_userInput:
            if i == " " or i == ".":
                if len(str) <= 3:
                    D_Output += str[::-1] + " "
                    str = ""
                elif len(str) > 6:
                    str = str[::-1]
                    for repeat in range(2):
                        temp = str[-4:]
                        str = str.replace(str[-4:], "", 1)
                        str = temp + str
                    D_Output += str + " "
                    str = ""
                else:
                    str = str[::-1]
                    val = str[len(str)-1]
                    str = str.replace(str[len(str)-1], "", 1)
                    str = str[:1] + val + str[1:]
                    D_Output += str + " "
                    str = ""
            else:
                str += i        
            
        return render(request, "decoder.html", {'D_Output': D_Output})
    else:
        return render(request, "decoder.html")

