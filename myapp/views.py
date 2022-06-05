from django.shortcuts import render
from .forms import UserRegisterForm,ProfileUpdateForm,UserUpdateForm
# Create your views here.
def register(request):
    '''
    This method will allow registration of users by rendering the template to display the registration form
    '''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Your Account Has Been Created.Proceed to Login!")
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {
        'form':form
    }
    return render(request,"users/register.html",context)