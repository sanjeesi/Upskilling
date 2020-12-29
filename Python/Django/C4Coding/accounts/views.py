from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth

# Create your views here.

def register(request):

    if request.method == 'POST':
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=email):
                print("Username taken")
            else:
                user = User.objects.create_user(username=email, password=password1, email=email)
                user.save()
                print("user created")
        else:
            print("Passwords not matching")
        return redirect("/")

    return render(request, "register.html")

def login(request):
    return render(request, "login.html")