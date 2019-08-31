from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        # model to be affected
        model=User

        # field i want in the form in order
        fields=['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    '''
    update username and email of the user 
    '''
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email']        