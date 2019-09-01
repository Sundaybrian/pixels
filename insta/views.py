from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Image,Comment,Like

# Create your views here.

def home(request):
  
    posts=Image.get_imgs()
    
    return render(request,'insta/home.html',{'posts':posts})

