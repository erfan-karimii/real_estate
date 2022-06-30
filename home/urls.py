from django.urls import path
from .import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('about_us', views.about, name='about'),
    path('our_team', views.team, name='team'),
    path('blog', views.blog, name='blog'),

]
