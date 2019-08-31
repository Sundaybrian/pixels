from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    # one user can have one profile and one profile is associated with one user
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    bio=models.TextField(max_length=140)
    profile_photo=models.ImageField(upload_to='profile_pics',default='default_profile.png')

    def __str__(self):
        return f'{self.user.username}-Profile'

    def save(self):
        '''
        overwrite save method to resize images
        '''
        super().save()

        img=Image.open(self.profile_photo.path)

        if img.height > 300 or img.width > 300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.profile_photo.path)







