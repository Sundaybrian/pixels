from django import forms
from .models import Image,tags

class NewInstaPost(forms.ModelForm):
    class Meta:
        model=Image
        exclude=['author','date_posted','last_modified','tags']
   

class AddTagsToPost(forms.ModelForm):
    '''
    attempt at adding tags to a post
    '''
    class Meta:
        model=tags
        fields=['tag_name']        