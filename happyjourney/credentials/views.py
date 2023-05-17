from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('login')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['Username']
        firstname = request.POST['First_Name']
        lastname = request.POST['Last_Name']
        email = request.POST['Email']
        password = request.POST['Password']
        cpassword = request.POST['Confirm Password']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname,
                                                email=email,
                                                password=password)
                user.save()
                return redirect('login')

        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('/')
    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
