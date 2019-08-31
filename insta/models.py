from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Q

# Create your models here.

class Image(models.Models):
    img_name=models.CharField(max_length=100)
    img_caption=models.TextField()
    image=models.ImageField(upload_to='images/',default='')
    date_posted=models.DateTimeField(auto_now_add=True)
    last_modified=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    likes=models.ForeignKey(Like)
    comments=models.ForeignKey(Comment)

    def __str__(self):
        return f'Image{self.image_name}--{self.image_caption}'
        

    def save_img(self):
        '''
        method to save an image
        '''
        self.save()

    def delete_img(self):
        '''
        method to delete an image
        '''
        self.delete()    


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
        method that returns photos based on a search query
        '''

        imgs=cls.objects.filter(Q(img_name__icontains=search_term)  | Q(author__username__icontains=search_term)  | Q(img_caption__icontains=search_term)  | Q(tags__tag_name__icontains=search_term))


