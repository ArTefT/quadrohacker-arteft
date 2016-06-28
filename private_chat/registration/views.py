# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User 
from .forms import UserForm, LoginForm
import models
import random
import string
from django.contrib.auth import authenticate, login
from django.db import IntegrityError

# Create your views here.

def registration(request):
    form = UserForm(data=request.POST or None)
    if request.method == 'GET':
        return render(request, 'registration/reg.html', {'form':form})
    if request.method == 'POST':
		#print request.POST
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		if password == '':
			password = password.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(8))
		try:
			user = User.objects.create_user(username, email, password) 
		except IntegrityError:
			return HttpResponse("<h1>Please, enter another username.</h1>")
		userprofile = models.UserProfile(username=username, email=email, password=password, user=user)
		userprofile.save()
		return render(request, 'registration/reg.html', {'form':form})

def login_view(request):
    form = LoginForm(data=request.POST or None)
    #сдесь ты данные из POST не достанешь нужно после if request.method == 'POST'
    #username = request.POST['username']
	#password = request.POST['password']
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
        else:
            return render(request, 'registration/login.html', {'form':form})
    else:
        return render(request, 'registration/login.html', {'form':form})
		 
