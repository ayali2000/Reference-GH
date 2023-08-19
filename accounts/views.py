from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from . forms import *
# Create your views here.
def signup(request):
    frm = SignUpForm()
    if request.method == "POST":
        frm = SignUpForm(request.POST)
        if frm.is_valid():
            frm.save()
            frm.clean()
            messages.success(request,'Account created successfully')
            return redirect('login')
        else:
            messages.success(request,'Account not created. Password must be strong, at least 8 characters and must contain numbers,letters and symbols')                
    else:
        frm = SignUpForm()
    context = {'frm':frm}    
        
    return render(request,'accounts/signup.html',context)




def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        try:
            if form.is_valid():
                user    = authenticate(username=form.data["username"], password=form.data["password"])
                if user:
                    login(request, user)
                    messages.success(request, "Login successful")
                    return redirect('/')
                messages.error(request, "Invalid credentials provided. Note that, both fields may be case-sensitive")
        except Exception as e:
            messages.error(request, "Invalid credentials provided. Note that, both fields may be case-sensitive")
                
   
    context = {
        "form":form
    }
    
    return render(request, "accounts/login.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")