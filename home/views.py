import re
from django.shortcuts import render
from posts.models import *
from admin_informations.models import *
# Create your views here.


def home(request):
    apartemans = aparteman.objects.filter(
        active=True).order_by('-upload_time')[0:3]
    vilaes = vilae.objects.filter(active=True).order_by('-upload_time')[0:3]
    zamins = zamin.objects.filter(active=True).order_by('-upload_time')[0:3]

    context = {
        "activebar": "home",
        'posts_zamin': zamins,
        'posts_vilaes': vilaes,
        'posts_apartemans': apartemans,
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about-us.html',{"activebar": "about"})

def team(request):
    people = AdminInformation.objects.all()
    return render(request, 'team.html',{'people':people})


def blog(request):
    return render(request,'blog.html')