from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    '''
    This method will allow registration of users
    '''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data['password1']
            login(request,User)
            messages.success(request,f"Your Account Has Been Created.Proceed  to Login!")
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {
        'form':form
    }
    return render(request,"users/register.html",context)


def login_page(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('post')
		else:
			messages.success(request, ("There Was An Error Logging In, Try Again..."))	
			return redirect('login')	


	else:
		return render(request, 'users/login.html', {})


def logoutUser(request):
	logout(request)
	return redirect('login')


#@login_required
def index(request):

    # Default view
    current_user = request.user
    posts = Post.objects.all()
    comments = Comment.get_comments()
    profiles = Profile.objects.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.post = Post.objects.get(id=int(request.POST["post_id"]))
            comment.save()
            return redirect('home')
    else:
        form = CommentForm()

    return render(request, 'index.html', {'current_user':current_user,'posts':posts, 'form':form, 'comments':comments,'profiles':profiles})

#@login_required()
def new_post(request):
    current_user = request.user
   
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user= current_user
            post.save()
        return redirect('home')
    else:
        form = NewPostForm()
    return render(request, 'posts/newpost.html', {'current_user':current_user, 'form':form})



#class based views for user uploading
class ImageCreateView(LoginRequiredMixin,CreateView):
    '''
    Class based view for adding new image
    '''
    model = Post
    fields = ['image','caption']

    def form_valid(self,form):
        '''
        form overide to set user who uploaded image
        '''
        form.instance.profile = self.request.user
        return super().form_valid(form)