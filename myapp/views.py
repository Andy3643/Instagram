from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView,DetailView
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
    if request.user.is_authenticated:
        return redirect('profile')
    
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
# def profile(request):
#     '''
#     This method handles the user profile 
#     '''
#     title = 'Profile'
#     if request.method == "POST":
#         u_form = UserUpdateForm(request.POST,instance=request.user)
#         p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request,f"You Have Successfully Updated Your Profile!")
#             return redirect('profile')
#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)
#     context = {
#         'title':title,
#         'u_form':u_form,
#         'p_form':p_form 
#     }
#     return render(request,'users/profile.html',context)

#@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile) 
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile') # Redirect back to profile page

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)








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



#@login_required
def CommentOnImage(request,pk):
    '''
    View for commenting on a specfic image
    '''
    current_user = request.user
    current_image = Post.objects.get(id=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.image = current_image
            comment.save()
            return redirect(index)
    else:       
        return redirect(index)
    
#@login_required
def OtherProfile(request,pk):
    '''
    Display user profile
    '''
    user = User.objects.get(pk=pk)
    users = User.objects.all()
    current_user = request.user
    posts = Post.objects.filter(profile=user)
    context = {
        "user":user,
        "posts":posts,
        "users":users,
        "current_user":current_user
    }
    return render(request,"users/profile.html",context)






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
    
class ImageDetailView(LoginRequiredMixin,DetailView):
    '''
    Class based view for viewing specific image with its details
    '''
    model = Post