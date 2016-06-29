# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages 
from .forms import UserForm, LoginForm
import models
import random
import string
from django.contrib.auth import authenticate, login
from django.db import IntegrityError

def random_password():
    password = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(8))
    return password

def registration(request):
    form = UserForm(data=request.POST or None)

    if request.method == 'POST':
        if form.is_valid(): # запускаем метод clean() из формы
            message = 'Registration success!'
		    #print request.POST
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            if password == '': 
                password = random_password()
            try: # пытаемся создать юзера
                user = User.objects.create_user(username, email, password)
            except: # если не вышло -- значит такой уже есть
                user = None
                message = 'This Username already exist' # создаем сообщение
                messages.error(request, message) # и добавляем его к request
            if user: # если юзер создался создаем и UserProfile
                userprofile = models.UserProfile(username=username, email=email, password=password, user=user)
                userprofile.save()
            return render(request, 'registration/reg.html', {'form':form ,'message':message})

    if request.method == 'GET' or not form.is_valid(): # тут если GET или форма в POST пришла невалидная
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
		 
