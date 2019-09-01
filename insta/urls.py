from django.urls import path
from . import views
from django.conf.urls import url
from .views import PostUpdateView,PostDeleteView

urlpatterns=[
    path('',views.home,name='insta-home'),
    path('post/new/',views.newInstaPost,name='new-insta-post'),
    path('post/<int:pk>/',views.postDetail,name='post-detail'),
    path('post/<int:pk>/update',views.PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete',views.PostDeleteView.as_view(),name='post-delete'),
    path('search/',views.search_results,name='search_results'),
    
]