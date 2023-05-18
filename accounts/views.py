from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout

# Create your views here.

def Register_users(request):

    if request.method == "POST":
        data = request.POST

        first_name_ = data.get('first_name')
        last_name_ = data.get('last_name')
        user_name_ = data.get('user_name')
        password_  = data.get('password')

        user = User.objects.filter(username = user_name_)

        if user.exists():
            messages.error(request, "Username already taken")
            return redirect('register')
       
        user = User.objects.create(
            first_name = first_name_,
            last_name = last_name_,
            username = user_name_
        )

        # converting normal password to encrypted(set_password())
        #to save password to model save()
        user.set_password(password_)
        user.save()
        messages.success(request, "Account created successfully!")

        return redirect('login')
    return render(request, "accounts/user_register.html")



def login_users(request):
   
    if request.method == 'POST':
        data = request.POST
        user_name_ = data.get('username')
        password_  = data.get('password')
        user = User.objects.filter(username = user_name_)
          
        #   exist is boolean return True or False
        if not user.exists():
            messages.success(request, "Invalid Username")
            return redirect('login')
       

        user = authenticate(username = user_name_, password = password_)
        # athenticate check if the user name and password are correct 
        # if not they will return none other wise return the correct object
       
        if user is None:
            messages.success(request, "Invalid Password")
            return redirect('login')
        
        else:
            login(request, user)
            messages.success(request, "successfully logged in")
            return redirect('recipe-page')

    return render(request, "accounts/user_login.html")



def logout_users(request):
    logout(request)
    return redirect('login')