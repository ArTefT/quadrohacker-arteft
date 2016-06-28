from django.shortcuts import render
from .models import UserMessage
from django.http import HttpResponse

def show_chat(request):
    messages_list = UserMessage.objects.order_by('-date_msg')[:25]
    output = ', '.join(q.text_msg for q in messages_list)
    return HttpResponse(output)
