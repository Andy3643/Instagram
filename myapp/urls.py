# from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
   path('home/',views.index,name='home'),
   path(r'', views.login_page, name='login'),#check if login working
   path(r'^register/', views.register, name='register'),
   path(r'^login/', views.login_page, name='login'),
   path(r'^logout/', views.logoutUser, name="logout"),
   path(r'^newpost/', views.new_post, name='new_post'),
   path(r'^user/(?P<pk>\d+)',views.OtherProfile,name="single_profile"),
   path(r'^image/(?P<pk>\d+)$',views.ImageDetailView.as_view(),name="image_detail"),
   path(r'^comment/(?P<pk>\d+)',views.CommentOnImage,name="image-comment"),
   path('profile/<username>/', views.profile, name='profile'),
  
   #path('user_profile/<username>/', views.user_profile, name='user_profile'),
   #path(r'^image/(\d+)',views.image,name ='image'),





]