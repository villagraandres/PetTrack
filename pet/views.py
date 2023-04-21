from django.shortcuts import render
#import Httpresponse
from django.http import HttpResponse
#import render
from django.shortcuts import render

# Create your views here.

def index(request):
    
    return render(request,'login/index.html')
