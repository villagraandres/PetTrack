from django.shortcuts import render
#import Httpresponse
from django.http import HttpResponse
#import render
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'login/index.html')

def register(request):
    if request.method=='POST':

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
            pass

       
    else:
        return render(request,'login/register.html')
    
