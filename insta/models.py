from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Image(models.Models):
    image_name=models.CharField(max_length=100)
    image_caption=models.TextField()
    image=models.ImageField(upload_to='images/',default='')
    date_posted=models.DateTimeField(auto_now_add=True)
    last_modified=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    likes=models.ForeignKey(Like)
    comments=models.ForeignKey(Comment)

    def __str__(self):
        return f'Image{self.image_name}--{self.image_caption}'

    @classmethod
    def get_imgs(cls):
         '''
         method that returns all photos in the db
         '''   
         imgs=cls.objects.order_by('date_posted')
         return imgs


    @classmethod
    def search(cls,search_term):
        '''
        method that returns 
        '''

