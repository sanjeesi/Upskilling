from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def register(request):

    if request.method == 'POST':
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=email).exists():
                messages.info(request, "Username taken..!!")
                return redirect("register")
            else:
                user = User.objects.create_user(username=email, password=password1, email=email)
                user.save()
                messages.info(request, "user created")
        else:
            messages.info(request, "Passwords not matching..!!")
            return redirect("register")
        return redirect("/")

    return render(request, "register.html")

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/courses/viewCourses")
        else:
            messages.info(request, "Invalid credentials!!")
            return redirect('login')
    else:
        return render(request, "login.html")