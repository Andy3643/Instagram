# from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns=[
   path('^$',views.post,name='post'),
   path(r'^register/', views.register, name='register'),
   path(r'^login/', views.login_page, name='login'),
   path(r'^logout/', views.logoutUser, name="logout"),
   path('profile/<username>/', views.profile, name='profile'),
   path('user_profile/<username>/', views.user_profile, name='user_profile'),
   path(r'^image/(\d+)',views.image,name ='image'),





]