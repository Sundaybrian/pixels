from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account Created for {username}')
            return redirect('insta-home')

    else:
                
        form=UserRegisterForm()
    return render(request,'user/register.html',{'form':form})

