# -*- coding:utf-8 -*-
from django.shortcuts import render
from .models import UserMessage
from django.http import HttpResponse
from registration.models import UserProfile
import forms

#TODO: во вьюхе show_chat() сделать форму для отправки сообщения
#      пример - вьюха регистрации. 
#      То есть show_chat() отдает последние сообщения,
#      и форму для создания сообщения.
#      Форму сделать отдельно в файле forms.py
          
def show_chat(request):
    form = forms.SendMessageForm()
    messages_list = UserMessage.objects.order_by('date_message')[:25]
    #output = ', '.join(q.text_msg for q in messages_list)
    if request.method=='GET':
        return render(request, 'chat/base.html', {'form':form, 'messages':messages_list})
    if request.method=='POST':
        if form:
            print 'VALID'
            user = UserProfile.objects.get(username=request.user.username)
            text = request.POST['text_message']
            UserMessage.objects.create(autor=user, text_message=text)
            messages_list = UserMessage.objects.order_by('date_message')[:25] 
            return render(request, 'chat/base.html', {'form':form, 'messages':messages_list})
        print 'NEVALID'
        return render(request, 'chat/base.html', {'form':form, 'messages':messages_list})
