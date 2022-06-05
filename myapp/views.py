from django.shortcuts import render,redirect
from .forms import UserRegisterForm,ProfileUpdateForm,UserUpdateForm
from django.contrib import messages
from .models import *
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
            login(request, user)
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

