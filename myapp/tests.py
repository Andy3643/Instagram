from django.test import TestCase
from .models import Post
from .models import User


class PostTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.user1 = User(username="sarahr")
        self.user1.save()
        self.post = Post(image='subaru',caption='Sunkissed',profile=self.user1)

    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.post,  Post))

    #Testing the save method
    def test_save_method(self):
        self.post.save_post()
        posts = Post.objects.all()
        self.assertTrue(len(posts)>0)

    #Testing the delete method
    def test_delete_method(self):
        self.post2 = Post(image='myself',caption='my ride',profile=self.user1)
        self.post2.save_post()
        self.post.save_post()
        self.post.delete_post()
        posts = Post.objects.all()
        self.assertEqual(len(posts),1)

