from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Q
from tinymce.models import HTMLField
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from django.urls import reverse


# Create your models here.

class tags(models.Model):
    '''
    models to create #tags to bind to photos
    '''
    tag_name=models.CharField(max_length=30)

    def __str__(self):
        return self.tag_name


class Image(models.Model):
    img_name=models.CharField(max_length=100)
    img_caption=HTMLField()
    poster=models.ImageField(upload_to='posters/',default='')
    date_posted=models.DateTimeField(auto_now_add=True)
    last_modified=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)

    def __str__(self):
        return f'Image{self.img_name}--{self.img_caption}'


    def get_absolute_url(self):
        '''
        fix for the get absolute url error after using the class view to update the view

            **thus creating a url for a model object **
            

        '''
        return reverse('post-detail',kwargs={'pk':self.pk})


    def save_img(self):
        '''
        method to save an image
        '''
        self.save()

    @classmethod
    def delete_img(cls,img_id):
        '''
        method to delete an image
        '''
        img=cls.objects.get(pk=img_id).delete()    


    @classmethod
    def get_imgs(cls):
         '''
         method that returns all photos in the db
         '''   
         imgs=cls.objects.order_by('date_posted')
         return imgs

    @classmethod
    def update_caption(cls,img_id,new_caption):
        '''
        method to update an image caption
        '''
        img=cls.objects.get(pk=img_id).update(img_caption=new_caption)
        img.save()

    @classmethod
    def search(cls,search_term):
        '''
        method that returns photos based on a search query
        '''

        imgs=cls.objects.filter(Q(img_name__icontains=search_term) |Q(author__username__icontains=search_term)  | Q(img_caption__icontains=search_term)  | Q(tags__tag_name__icontains=search_term))

        return imgs

    @classmethod
    def get_img_by_id(cls,id):


        try:
            img=Image.objects.get(id=id)
            
        except ObjectDoesNotExist:
             raise Http404()
             assert False

        return img    
            
            


class Comment(models.Model):
    '''
    model to create comments
    '''  
    image=models.ForeignKey(Image,on_delete=models.CASCADE),
    comment_owner=models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    comment_content=models.CharField(max_length=300,blank=True)
    

    def save_comment(self):
        '''
        method to save a comment
        '''
        self.save()

    @classmethod
    def delete_comment(cls,comment_id):
        '''
        method to delete a comment
        '''
        comment=cls.objects.get(pk=comment_id)
        comment.delete()    


    @classmethod
    def get_comments(cls,img_id):
        '''
        method to fetch all comments associated with a given img
        '''    
        comments=cls.objects.filter(pk=img_id).all()
        return comments 

    def __str__(self):
        return self.comment_content          


class Like(models.Model):
    '''
    models to create likes to bind to photos
    '''
    liker=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ForeignKey(Image,on_delete=models.CASCADE)



        
    











