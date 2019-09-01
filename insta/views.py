from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.contrib import messages
from .models import Image,Comment,Like
from django.contrib.auth.decorators import login_required
from .forms import NewInstaPost,AddTagsToPost

# Create your views here.

def home(request):
  
    posts=Image.get_imgs()
    
    return render(request,'insta/home.html',{'posts':posts})


@login_required
def newInstaPost(request):
    current_user=request.user
    if request.method=='POST':
        form=NewInstaPost(request.POST,request.FILES)
        tagForm=AddTagsToPost(request.POST)
        if form.is_valid() and tagForm.is_valid():
            img_name=form.cleaned_data.get('img_name')
            img=form.save(commit=False)
            img.author=current_user

            img.save()
            tagForm.save()

            messages.success(request,f'Post Created for {img_name}')
        return redirect('insta-home')    
    else:
        form=NewInstaPost()
        tagForm=AddTagsToPost()
    return render(request,'insta/new_insta.html',{'form':form,'tagForm':tagForm})   


def postDetail(request,pk):
    '''
    view function that leads to a single post
    '''
    try:
        img=Image.objects.get(id=pk)
        
    except ValueError:
        raise Http404()
        assert False
    
    return render(request,'insta/post-detail.html',{'post':img})



