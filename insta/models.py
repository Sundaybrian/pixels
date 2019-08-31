from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Q


# Create your models here.

class Image(models.Model):
    img_name=models.CharField(max_length=100)
    img_caption=models.TextField()
    image=models.ImageField(upload_to='images/',default='')
    date_posted=models.DateTimeField(auto_now_add=True)
    last_modified=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    # likes=models.ForeignKey(Like)
    # comments=models.ForeignKey(Comment)
    # tags=models.ManyToManyField(tags)

    def __str__(self):
        return f'Image{self.img_name}--{self.img_caption}'


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


class tags(models.Model):
    '''
    models to create #tags to bind to photos
    '''
    tag_name=models.CharField(max_length=30)

    def __str__(self):
        return self.tag_name

class Like(models.Model):
    '''
    models to create likes to bind to photos
    '''
    like=models.IntegerField()

    def save_like(self):
        '''
        saving a like
        '''
        
    

class Comment(models.Model):
    '''
    model to create comments
    '''   
    comment_content=models.TextField()

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









