from django.shortcuts import render
from django.http import HttpResponse,Http404

# Create your views here.

posts=[
    {
        'username':'Brians Brians',
        'title':'Out and About',
        'poster_path':'static/img/ironman1.jpg',
        'date_posted':'August 31,2019'
    },
      {
        'username':'Brians Omwami',
        'title':'iron man',
        'poster_path':'static/img/ironman1.jpg',
        'date_posted':'August 29,2019'
    }
    ,
      {
        'username':'Sunday Omwami',
        'title':'iron man',
        'poster_path':'static/img/ironman1.jpg',
        'date_posted':'August 30,2019'
    }

]

def home(request):
    return render(request,'insta/home.html',{'posts':posts})

