from xml.parsers.expat import model
from django.db import models
from django.contrib.auth.models import User
import datetime as dt
import django.utils.timezone


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default='')
    image = models.ImageField(upload_to = 'posts/', default='No Image')
    caption = models.CharField(max_length=120)
    likes = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)
     
       
    def save_post(self):
        '''
        method to save new post in the db
        '''
        self.save()

    def delete_post(self):
        '''
        method to delete saved post from db
        '''
        self.delete()
    
    @classmethod
    def update_post(self, update):
        '''
        update saved post in db
        '''
        self.post = update
        self.save
        
    @classmethod
    def get_posts(cls):
        '''
        method to get posts from db
        '''
        posts = cls.objects.all()
        return posts
    @classmethod
    def display_user_post(cls):
        post = cls.objects.filter()
        return post