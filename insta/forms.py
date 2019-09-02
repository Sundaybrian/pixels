from django import forms
from .models import Image,tags,Comment

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


class NewComment(forms.ModelForm):
    '''
    form to create a comment
    '''
    class Meta:
        model=Comment
        fields=['comment_content']        