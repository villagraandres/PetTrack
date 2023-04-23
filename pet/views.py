from django.shortcuts import render
#import Httpresponse
from django.http import HttpResponse
#import render
from django.shortcuts import render
#import models
from .models import User
import secrets
import string


# Create your views here.

def index(request):
    return render(request,'login/index.html')

def register(request):
    if request.method=='POST':
        username=request.POST['name'];
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
            user = User(username=username,email=email,code=code)
            user.set_password(password)
            user.save();
            return render(request,'login/mail.html',{'mail':email})

       
    else:
        return render(request,'login/register.html')
    
