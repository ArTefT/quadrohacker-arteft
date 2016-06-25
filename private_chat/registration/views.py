from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
import models
# Create your views here.

def registration(request):
    form = UserForm(data=request.POST or None)
    if request.method == 'GET':
        return render(request, 'registration/reg.html', {'form':form})
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = models.UserProfile(username=username, email=email, password=password, user=None)
        user.save()
        return render(request, 'registration/reg.html', {'form':form})
              
