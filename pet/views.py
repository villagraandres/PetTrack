from django.shortcuts import render
#import Httpresponse
from django.http import HttpResponse
#import render
from django.shortcuts import render
#import models
from .models import User
import secrets
import string
from django.core.mail import send_mail
from django.db import IntegrityError
from django.contrib.auth import login



# Create your views here.

def index(request):
    return render(request,'login/index.html')

def register(request):
    if request.method=='POST':
        firstname=request.POST['name'];
        email=request.POST['email'];
        password=request.POST['password'];
        

        inputs=['name','email','password','password2']
        errors=[]
        for i in inputs:
            if not request.POST.get(i):
                message=f"{i} is obligatory"
                errors.append(message.capitalize())
        if request.POST.get('password')!=request.POST.get('password2'):
            errors.append("Passwords don't match")
        if len(errors)>=1:     
            return render(request,'login/register.html',{'errors':errors})
        else:
            alphabet = string.ascii_letters + string.digits
            code = ''.join(secrets.choice(alphabet) for i in range(16))
            try:
                user = User(username=email,first_name=firstname,email=email,code=code)
                user.set_password(password)
                user.save();
            except IntegrityError:
                return render(request,'login/register.html',{'error':'Email already exists'})
            
            activation_link = f'http://127.0.0.1:8000/confirm/{code}'

            send_mail(
                "Confirm your Account",
                "",
                "from@example.com",
                [email],
                fail_silently=False,
                html_message=f" <h1>Hi {firstname} your account has been created!</h1> <p>Click <a href='{activation_link}'>here</a> to activate it</p>"
            )
            return render(request,'login/email.html',{'mail':email})

       
    else:
        return render(request,'login/register.html')
    

def email(request):
    pass

def confirm(request,num):
    try:
        user=User.objects.get(code=num)
    except User.DoesNotExist:
        return render(request,'login/confirm.html',{'message':'This is code is invalid or is already has been used'})
    else:
        user.auth = True
        user.code=''
        user.save()
        login(request,user)
        return render(request, 'login/confirm.html', {'message': 'Your account has been confirmed'})
    


def home(request):
    return render(request,'auth/home.html');