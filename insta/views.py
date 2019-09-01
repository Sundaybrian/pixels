from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Image,Comment,Like
from django.contrib.auth.decorators import login_required
from .forms import NewInstaPost

# Create your views here.

def home(request):
  
    posts=Image.get_imgs()
    
    return render(request,'insta/home.html',{'posts':posts})


@login_required
def newInstaPost(request):
    current_user=request.user
    if request.method=='POST':
        form=NewInstaPost(request.POST,request.FILES)
        if form.is_valid():
            img=form.save(commit=False)
            img.author=current_user
            img.save()
        return redirect('insta-home')    
    else:
        form=NewInstaPost()
    return render(request,'insta/new_insta.html',{'form':form})        




