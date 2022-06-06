from xml.parsers.expat import model
from django.db import models
from django.contrib.auth.models import User
import datetime as dt
import django.utils.timezone
from cloudinary.models import CloudinaryField


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default='')
    #image = CloudinaryField('image',default='No Image')
    image=models.ImageField(upload_to='posts/')
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
    
    
LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    comment = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()
        
    @classmethod
    def get_comments(cls):
        comments = cls.objects.all()
        return 
    
    def __str__(self):
        return self.comment

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    profile_pic=models.ImageField(upload_to='pictures/',default='default.png')
    #photo = CloudinaryField('image',default='No Image')
    bio = models.TextField(max_length=255)

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save_profile(self):
        '''
        add new profile to db
        '''
        self.save()

    def delete_profile(self):
        '''
        delete  user from db
        '''
        self.delete()

    def updateProfile(self, update):
       self.bio = update
       self.photo = update
       self.save

    @classmethod
    def search_profile(cls, search_term):
        user = cls.objects.filter(user__username__icontains=search_term)
        return user 

    @classmethod
    def get_by_id(cls, id):
        profile = cls.objects.get(id=id)
        return profile

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null = True)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10, null = True)

    def __str__(self):
        return self.post
    
class Follow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return f'{self.follower} Follow'