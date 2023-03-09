from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        userName = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username= userName, password= password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Enter valid credentials')
            return redirect('login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        userName = request.POST['username']
        firstName = request.POST['first_name']
        lastName = request.POST['last_name']
        emailId = request.POST['email']
        password = request.POST['password']
        confirmPswd = request.POST['confirm_pswd']

        if password == confirmPswd:
            if User.objects.filter(username= userName).exists():
                messages.info(request, 'Username already exits')
                return redirect('register')
            elif User.objects.filter(email= emailId).exists():
                messages.info(request, 'email already exits')
                return redirect('register')
            else:
                user = User.objects.create_user(username=userName, first_name=firstName, last_name=lastName,email=emailId, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')



    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')