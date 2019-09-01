from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.contrib import messages
from .models import Image,Comment,Like
from django.contrib.auth.decorators import login_required
from .forms import NewInstaPost,AddTagsToPost
from django.core.exceptions import ObjectDoesNotExist

from django.views.generic import UpdateView,DeleteView
from django.contrib.auth.mixins import (LoginRequiredMixin,UserPassesTestMixin)
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


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    '''
    class view method to update the post form
        declare the model to be affected
        declare the template to be used
        declare fields in the model to be affected
    '''
    model=Image
    template_name='insta/post-update.html'
    fields=['img_name','img_caption','poster']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        '''
        check to see if the current user is the owner of the post
        '''    
        post=self.get_object()
        return self.request.user==post.author


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    '''
    class view method to update the post form
        declare the model to be affected
        declare the template to be used
        declare fields in the model to be affected
    '''
    model=Image
    template_name='insta/post-confirm-delete.html'
    success_url='/'

    def test_func(self):
        '''
        check to see if the current user is the owner of the post
        '''    
        post=self.get_object()
        return self.request.user==post.author



def postDetail(request,pk):
    '''
    view function that leads to a single post
    #     
    '''
    img=Image.get_img_by_id(pk)
   
    return render(request,'insta/post-detail.html',{'post':img,'user':request.user})



