from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def login(request):
    if request.method == 'POST':
        password = request.POST['password']
        username = request.POST['username']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'you are now login')
            return redirect('dashboard')
        else:
            messages.error(request, 'invalid username or password')
            return redirect('login')

    return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'username is already exist')
                return redirect('register')
            else:
                if User.objects.filter(email=email):
                    messages.error(request, 'Email is already exist')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email,
                                                    username=username, password=password)
                    auth.login(request, user)
                    messages.success(request, 'your now login')
                    user.save()
                    return redirect('dashboard')

                    # messages.success(request, 'your register success')
                    # return redirect('login')

        else:
            messages.error(request, 'password do not match')
            return redirect('register')


    else:
        return render(request, 'accounts/register.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def logout(request):
    return render(request, 'accounts/logout.html')
