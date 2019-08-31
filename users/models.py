from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    # one user can have one profile and one profile is associated with one user
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    bio=models.TextField(max_length=140)
    profile_photo=models.ImageField(upload_to='profile_pics',default='')

    def __str__(self):
        return f'{self.user.username} Profile'




