# -*- coding:utf-8 -*-
from django.shortcuts import render
from .models import UserMessage
from django.http import HttpResponse

#TODO: во вьюхе show_chat() сделать форму для отправки сообщения
#      пример - вьюха регистрации. 
#      То есть show_chat() отдает последние сообщения,
#      и форму для создания сообщения.
#      Форму сделать отдельно в файле forms.py
          

def show_chat(request):
    messages_list = UserMessage.objects.order_by('-date_msg')[:25]
    output = ', '.join(q.text_msg for q in messages_list)
    return HttpResponse(output)
