from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns=[
    path('',views.home,name='insta-home'),
    path('post/new/',views.newInstaPost,name='new-insta-post'),
    path('post/<int:pk>/',views.postDetail,name='post-detail'),
    
]