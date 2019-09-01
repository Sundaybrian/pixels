from django import forms
from .models import Image

class NewInstaPost(forms.ModelForm):
    class Meta:
        model=Image
        exclude=['author','date_posted']
        widgets={
            'tags':forms.CheckboxSelectMultiple(),
        }