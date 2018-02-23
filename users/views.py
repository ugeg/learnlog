from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.forms import UserCreationForm
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('learnlogs:index'))
def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticate_user = authenticate(username=new_user,password=request.POST['password1'])
            login(request,authenticate_user)
            return HttpResponseRedirect(reverse('learnlogs:index'))
    context = {'form':form}
    return render(request,'users/register.html',context)

# Create your views here.
