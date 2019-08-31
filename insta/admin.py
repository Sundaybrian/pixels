from django.contrib import admin
from .models import Comment,Image,tags,Like


# Register your models here.

admin.site.register(Comment)
admin.site.register(Image)
admin.site.register(tags)
admin.site.register(Like)
